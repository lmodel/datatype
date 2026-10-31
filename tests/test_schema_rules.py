"""Checks that the adapt copy can sit beside LOKF and the neighbours' copies."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent

# What a host may import beside this schema's adapt copy: LOKF's schema, pinned
# by the sidecar, and the adapt copies other lmodel repositories release. Each
# neighbour is the schema asset of a release, downloaded and checked against
# the release's .sha256 and its build-provenance attestation, and pinned here
# by that checksum.
COPY = ROOT / ".lokf" / "datatype.yaml"
LOKF = ROOT / ".lokf" / "lokf.yaml"
NEIGHBOURS = {
    # lmodel/slsa v0.8.0, schema-v0.8.0-slsa.yaml
    "slsa.yaml": "16a3c50a4592dbeffeeee0e9d3d354efe71ae3efcc8eb272ed9b782117d8a024",
    # lmodel/github-actions v0.3.0, schema-v0.3.0-github-actions.yaml
    "github-actions.yaml": "52224e53939325f56d3470ed6ddd2041cdd53ae7cdb0ac72773829100798452e",
    # lmodel/oscal v0.1.2, schema-v0.1.2-oscal.yaml
    "oscal.yaml": "4eb56d7d1106463ed0a2255a29af14b8d619741acc29863d1e86eb3f8923c710",
    # lmodel/spdx v0.1.0, schema-v0.1.0-spdx.yaml
    "spdx.yaml": "3411cf5d19b1955f0362988c542984e4c817417c7b7b7892647aba1adf1ddd4a",
    # lmodel/nist-sp-800-218 v0.1.1, schema-v0.1.1-nist-sp-800-218.yaml
    "nist-sp-800-218.yaml": "479824cdd95e52226a35ff3a471b7ce93239635ccd5db7ac72a8143cdd1d8495",
    # lmodel/nist-sp-800-53 v0.1.0, schema-v0.1.0-nist-sp-800-53.yaml
    "nist-sp-800-53.yaml": "d32a989b5b855281cb45d707bf59cf52b125f05a09c54930e2b4d45c174c0d99",
    # lmodel/nist-sp-800-171 v0.1.0, schema-v0.1.0-nist-sp-800-171.yaml
    "nist-sp-800-171.yaml": "d204efa6653692da665f8604a8fb8bf445f04b37f41460a5ce2853a014b2982f",
    # lmodel/nist-csf-v2 v0.1.0, schema-v0.1.0-nist-csf-v2.yaml
    "nist-csf-v2.yaml": "5f6bba4c4721f65665c3a0a702ca6b15df5b488048fed454acfe4cc69f7ca9c7",
    # lmodel/in-toto v0.1.1, schema-v0.1.1-in-toto.yaml
    "in-toto.yaml": "feb2711d782643dfeb670648508540f29393c437aaceae5318849f62e8e14c6d",
    # lmodel/cis-controls v0.2.0, schema-v0.2.0-cis-controls.yaml
    "cis-controls.yaml": "fbb325b4e55860381293b98f3be9c5b37e12903d3d88228d0e15a761dc80dc98",
    # lmodel/iso27001 v0.1.0, schema-v0.1.0-iso27001.yaml
    "iso27001.yaml": "f5ca519043cd994c41f286f84ebc2ea510121bd2129d83c017f73a3d24ee2fe1",
    # lmodel/stix v0.1.0, schema-v0.1.0-stix.yaml
    "stix.yaml": "3837d097c0cd48e0d2a98d118003c099d1290333f5b973aee85a7017bae344c9",
    # lmodel/attack v0.1.0, schema-v0.1.0-attack.yaml
    "attack.yaml": "c2e436b0d8ab0e60a8d6557b3ba32894e0b0d23b866f1e0c0d608a97e9f5f08e",
}
NEIGHBOUR_DIR = ROOT / "tests" / "neighbours"
ELEMENT_KINDS = ("classes", "enums", "types", "subsets")

# Keys the copy shares with a neighbour. LinkML keeps one namespace, and the
# JSON-LD context gives each key one IRI across a composite, whether it is a
# slot or an attribute on either side, so a shared key projects under one
# vocabulary's IRI. The copy shares `value`, the ontology's data:value, with
# six neighbours, each under its own IRI, so a host imports this copy beside
# none of them until lokf adapt can rename what a neighbour defines (lokf
# issue 169, `--beside`). A new overlap fails the test. title and
# description are not the copy's keys: lokf adapt folds both into LOKF's
# slots of the same IRI.
SHARED_WITH_NEIGHBOURS = {name: set() for name in NEIGHBOURS}
for name in (
    "attack.yaml",
    "in-toto.yaml",
    "oscal.yaml",
    "slsa.yaml",
    "spdx.yaml",
    "stix.yaml",
):
    SHARED_WITH_NEIGHBOURS[name] = {"value"}

# What `lokf adapt` renames because lokf.yaml defines the name, each keeping
# the ontology's IRI.
RENAMED_CLASSES = {"DatatypeConcept": ("Concept", "data:Concept")}
RENAMED_SLOTS = {"datatype_unit": ("unit", "data:unit")}

MAPPING_KEYS = (
    "mappings",
    "exact_mappings",
    "close_mappings",
    "related_mappings",
    "narrow_mappings",
    "broad_mappings",
)


def _load(path):
    return yaml.safe_load(path.read_text())


def _expander(doc):
    """A function that expands a CURIE by the prefixes a schema file binds."""
    prefixes = doc.get("prefixes") or {}

    def expand(curie):
        prefix, _, local = curie.partition(":")
        return prefixes[prefix] + local if prefix in prefixes else curie

    return expand


def _names(path):
    """Each kind of element a schema file declares, and every slot and
    attribute name with the IRI it expands to."""
    doc = _load(path)
    expand = _expander(doc)
    default = doc.get("default_prefix")
    elements = {kind: set(doc.get(kind) or {}) for kind in ELEMENT_KINDS}
    slots = {}
    owners = [doc.get("slots") or {}]
    owners += [
        (cls or {}).get("attributes") or {}
        for cls in (doc.get("classes") or {}).values()
    ]
    for owner in owners:
        for name, slot in owner.items():
            uri = (slot or {}).get("slot_uri") or f"{default}:{name}"
            slots.setdefault(name, set()).add(expand(uri))
    return elements, slots


def _mappings(node):
    """Every mapping value anywhere in a parsed schema file."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key in MAPPING_KEYS:
                yield from value if isinstance(value, list) else [value]
            else:
                yield from _mappings(value)
    elif isinstance(node, list):
        for item in node:
            yield from _mappings(item)


def test_neighbours_are_the_released_assets():
    """Each neighbour copy is byte for byte the asset its release published."""
    assert {p.name for p in NEIGHBOUR_DIR.iterdir()} == set(NEIGHBOURS)
    for name, sha256 in NEIGHBOURS.items():
        digest = hashlib.sha256((NEIGHBOUR_DIR / name).read_bytes()).hexdigest()
        assert digest == sha256, name


def test_names_apart_from_lokf():
    """No class, enum, type or subset name of the copy is LOKF's, and a slot
    name the two share carries LOKF's IRI."""
    elements, slots = _names(COPY)
    their_elements, their_slots = _names(LOKF)
    for kind in ELEMENT_KINDS:
        assert not elements[kind] & their_elements[kind], kind
    for name in slots.keys() & their_slots.keys():
        assert slots[name] == their_slots[name], name


def test_names_apart_from_neighbours():
    """A class, enum, type or subset name is the copy's alone, and the only
    keys it shares with a neighbour are the listed ones."""
    elements, slots = _names(COPY)
    for name in NEIGHBOURS:
        their_elements, their_slots = _names(NEIGHBOUR_DIR / name)
        for kind in ELEMENT_KINDS:
            assert not elements[kind] & their_elements[kind], (name, kind)
        assert slots.keys() & their_slots.keys() == SHARED_WITH_NEIGHBOURS[name], name


def test_copy_renames_what_lokf_defines_and_keeps_the_iris():
    """Concept and unit, which lokf.yaml defines, are renamed in the copy,
    keep the ontology's IRIs and name their old names as aliases."""
    doc = _load(COPY)
    for new, (old, uri) in RENAMED_CLASSES.items():
        assert doc["classes"][new]["class_uri"] == uri
        assert doc["classes"][new]["aliases"] == [old]
        assert old not in doc["classes"]
    for new, (old, uri) in RENAMED_SLOTS.items():
        assert doc["slots"][new]["slot_uri"] == uri
        assert doc["slots"][new]["aliases"] == [old]
        assert old not in doc["slots"]


def test_copy_is_rooted_on_nothing():
    """Every class is a value a concept holds, so the copy re-roots no class
    on Concept, no slot is an identifier that would make adapt root one, and
    the copy imports nothing but the LinkML types and LOKF."""
    doc = _load(COPY)
    assert not [n for n, c in doc["classes"].items() if c.get("is_a") == "Concept"]
    assert not [n for n, s in doc["slots"].items() if s.get("identifier")]
    assert doc["imports"] == ["linkml:types", "lokf"]


def test_mappings_use_a_bound_prefix():
    """Every mapping in the copy is a CURIE whose prefix the copy binds. A full
    address that no prefix covers makes every `lokf convert --schema` over the
    copy warn that it has no namespace. The copy carries none today, since
    the ontology states no alignment (tests/test_upstream.py)."""
    doc = _load(COPY)
    prefixes = doc.get("prefixes") or {}
    for mapping in _mappings(doc):
        prefix, sep, _ = mapping.partition(":")
        assert sep and prefix in prefixes, mapping
