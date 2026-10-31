"""The schema held to the copy of the Datatype Ontology in upstream/.

The copy is checked against the watch's pins, the schema header against the
watch, and the schema against the ontology's Turtle file: the same classes
and properties with the same IRIs, labels and definitions, the same ranges
and super-properties, and the restrictions on each class as the slots,
cardinalities, ranges and fixed values LinkML states.
"""

import hashlib
import importlib.util
import re
from functools import cache
from pathlib import Path

import pytest
import yaml
from linkml_runtime import SchemaView
from rdflib import OWL, RDF, RDFS, SKOS, XSD, BNode, Graph, URIRef
from rdflib.namespace import DCTERMS

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "datatype" / "schema" / "datatype.yaml"
COPY = ROOT / "upstream"
TURTLE = COPY / "rdf" / "datatype.ttl"
ONTOLOGY = URIRef("http://linked.data.gov.au/def/datatype")

# The LinkML range each OWL range renders as. A class of individuals, such
# as skos:Concept or a union of SKOS and OWL classes, becomes an IRI, since
# the validator cannot check what an IRI names.
XSD_RANGES = {
    XSD.boolean: "boolean",
    XSD.decimal: "decimal",
    XSD.integer: "integer",
    XSD.string: "string",
}


def _watch():
    spec = importlib.util.spec_from_file_location(
        "watch_pins", ROOT / "scripts" / "check_upstream_release.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


WATCH = _watch()


@cache
def graph() -> Graph:
    return Graph().parse(TURTLE, format="turtle")


@cache
def view() -> SchemaView:
    return SchemaView(str(SCHEMA))


@cache
def header() -> dict:
    return yaml.safe_load(SCHEMA.read_text())


def _owl_range(node) -> str:
    return XSD_RANGES.get(node, "uriorcurie")


def _iri(curie: str) -> str:
    return view().expand_curie(curie)


def _classes() -> dict[str, str]:
    """Each schema class by the IRI its class_uri names."""
    return {_iri(c.class_uri): c.name for c in view().all_classes().values()}


def _slots() -> dict[str, str]:
    """Each schema slot by the IRI its slot_uri names."""
    return {_iri(s.slot_uri): s.name for s in view().all_slots().values()}


def _text(node, predicate) -> str:
    return str(graph().value(node, predicate)).strip()


# --------------------------------------------------------------------------
# The copy, the header and the watch agree.


def _blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


@pytest.mark.parametrize("name", sorted(WATCH.PINNED_BLOBS))
def test_the_copy_matches_its_pin(name):
    assert _blob_sha(COPY / name) == WATCH.PINNED_BLOBS[name]


def test_the_copy_holds_only_pinned_files():
    held = {p.relative_to(COPY).as_posix() for p in COPY.rglob("*") if p.is_file()}
    assert held == set(WATCH.PINNED_BLOBS)


def test_the_header_names_the_pinned_edition():
    """The header's version and source are the watch's pins, the version is
    the copy's dcterms:modified date, and the source is the ontology's IRI."""
    assert header()["version"] == WATCH.PINNED_EDITION
    assert header()["source"] == WATCH.PINNED_SOURCE == str(ONTOLOGY)
    assert _text(ONTOLOGY, DCTERMS.modified) == WATCH.PINNED_EDITION
    assert _text(ONTOLOGY, DCTERMS.created) == header()["annotations"]["upstream_created"]
    assert header()["annotations"]["upstream_commit"] == WATCH.PINNED_COMMIT
    assert header()["annotations"]["upstream_branch"] == WATCH.PINNED_BRANCH
    assert WATCH.PINNED_COMMIT in " ".join(header()["see_also"])


def test_the_ontology_states_no_version_and_the_licence_notice_holds():
    """The ontology has no versionInfo or versionIRI, so the date stands in
    for one, and it states CC0 as the header's annotation says."""
    assert graph().value(ONTOLOGY, OWL.versionInfo) is None
    assert graph().value(ONTOLOGY, OWL.versionIRI) is None
    licence = str(graph().value(ONTOLOGY, DCTERMS.license))
    assert licence == "http://creativecommons.org/publicdomain/zero/1.0/"
    assert "CC0-1.0" in header()["annotations"]["upstream_licence"]
    assert "Attribution 4.0 International" in (COPY / "LICENSE").read_text()


def test_the_prefix_is_the_ontologys_own():
    """The schema binds data: to the namespace the ontology binds it to."""
    bound = dict(graph().namespaces())
    assert header()["prefixes"]["data"] == str(bound["data"])


# --------------------------------------------------------------------------
# The schema renders every class and property, and nothing else.


def test_the_classes_are_the_ontologys():
    owl_classes = {
        str(c) for c in graph().subjects(RDF.type, OWL.Class) if isinstance(c, URIRef)
    }
    assert set(_classes()) == owl_classes
    for iri, name in _classes().items():
        assert name == iri.rsplit("/", 1)[1], "a class keeps its local name"


def _properties() -> set[URIRef]:
    return {
        p
        for kind in (OWL.DatatypeProperty, OWL.ObjectProperty)
        for p in graph().subjects(RDF.type, kind)
    }


def test_the_slots_are_the_ontologys_properties_and_rdf_value():
    """Each property is a slot of the same local name, and rdf:value, which
    the ontology restricts on Concept and names as a super-property, is the
    one slot from outside it."""
    expected = {str(p) for p in _properties()} | {str(RDF.value)}
    assert set(_slots()) == expected
    for iri, name in _slots().items():
        if iri != str(RDF.value):
            assert name == iri.rsplit("/", 1)[1], "a slot keeps its local name"
    assert _slots()[str(RDF.value)] == "rdf_value"


@pytest.mark.parametrize("kind", ["class", "slot"])
def test_titles_and_descriptions_are_the_ontologys(kind):
    """Each title is the term's rdfs:label, and each description its
    skos:definition, trimmed."""
    terms = _classes() if kind == "class" else _slots()
    for iri, name in terms.items():
        if iri == str(RDF.value):
            continue
        element = view().get_element(name)
        assert element.title == _text(URIRef(iri), RDFS.label), name
        assert element.description == _text(URIRef(iri), SKOS.definition), name


def test_ranges_and_super_properties_are_the_ontologys():
    """A datatype property's range is its XSD range or none, an object
    property's is an IRI, and is_a names the super-property. The ontology
    states no domain, and neither does the schema."""
    for prop in _properties():
        slot = view().get_slot(_slots()[str(prop)])
        owl_range = graph().value(prop, RDFS.range)
        if (prop, RDF.type, OWL.ObjectProperty) in graph():
            assert slot.range == "uriorcurie", slot.name
        elif owl_range is None:
            assert slot.range is None, slot.name
        else:
            assert slot.range == _owl_range(owl_range), slot.name
        parents = list(graph().objects(prop, RDFS.subPropertyOf))
        if parents:
            assert len(parents) == 1
            assert _iri(view().get_slot(slot.is_a).slot_uri) == str(parents[0]), slot.name
        else:
            assert slot.is_a is None, slot.name
        assert graph().value(prop, RDFS.domain) is None
        assert slot.domain is None


def _restrictions(cls: URIRef) -> dict[str, dict]:
    """Every restriction on a class and its named superclasses, by property:
    its cardinality, maximum cardinality, allValuesFrom and hasValue."""
    found: dict[str, dict] = {}
    for parent in graph().objects(cls, RDFS.subClassOf):
        if isinstance(parent, BNode):
            prop = str(graph().value(parent, OWL.onProperty))
            for key, predicate in (
                ("cardinality", OWL.cardinality),
                ("max", OWL.maxCardinality),
                ("only", OWL.allValuesFrom),
                ("value", OWL.hasValue),
            ):
                if (obj := graph().value(parent, predicate)) is not None:
                    found.setdefault(prop, {}).setdefault(key, obj)
        else:
            for prop, facts in _restrictions(parent).items():
                for key, obj in facts.items():
                    found.setdefault(prop, {}).setdefault(key, obj)
    return found


def test_superclasses_are_the_ontologys():
    for iri, name in _classes().items():
        named = [p for p in graph().objects(URIRef(iri), RDFS.subClassOf) if isinstance(p, URIRef)]
        cls = view().get_class(name)
        parent = [_iri(view().get_class(cls.is_a).class_uri)] if cls.is_a else []
        assert parent == [str(p) for p in named], name


@pytest.mark.parametrize(
    "name", ["Boolean", "Concept", "Count", "Percent", "PercentRange",
             "QuantitativeMeasure", "QuantitativeRange", "Text"],
)
def test_restrictions_are_the_classs_slots(name):
    """A class's slots are the properties its restrictions name. Exactly one
    is required and single, at most one is single, allValuesFrom is the
    range, and hasValue the one value a pattern allows."""
    cls = URIRef(_iri(view().get_class(name).class_uri))
    restrictions = _restrictions(cls)
    slots = {_iri(view().induced_slot(s, name).slot_uri): s for s in view().class_slots(name)}
    assert set(slots) == set(restrictions), name
    for prop, facts in restrictions.items():
        slot = view().induced_slot(slots[prop], name)
        if "cardinality" in facts:
            assert int(facts["cardinality"]) == 1
            assert slot.required and not slot.multivalued, slot.name
        else:
            assert not slot.required, slot.name
        if "max" in facts:
            assert int(facts["max"]) == 1
            assert not slot.multivalued, slot.name
        if "only" in facts:
            assert slot.range == _owl_range(facts["only"]), slot.name
        if "value" in facts:
            assert slot.pattern == f"^{re.escape(str(facts['value']))}$", slot.name


# --------------------------------------------------------------------------
# Mappings.


def test_the_schema_maps_nothing():
    """The ontology states no alignment to another vocabulary beyond
    rdf:value, which is_a renders, so the schema carries no mapping. A
    mapping added later comes with a hash-pinned term list to test it."""
    keys = ("exact_mappings", "close_mappings", "related_mappings",
            "narrow_mappings", "broad_mappings", "mappings")
    for element in view().all_elements().values():
        if element.from_schema == "https://w3id.org/linkml/types":
            continue
        for key in keys:
            assert not getattr(element, key, None), (element.name, key)
