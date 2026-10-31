<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# datatype

AGLDWG Datatype Ontology (LinkML)

> **Two ways in.** This README is one; the other is a docent, a museum's name
> for a guide. Install
> [`ktl-docent`](https://github.com/noelmcloughlin/knowledge-trust-ladder) into
> whatever agent you already use, by a route from
> [the install page](https://w3id.org/ktl/docs/install/), and ask it anything
> about this project. It answers from `.lokf/knowledge/`,
> the checked part of what the project knows, and says how far each answer has
> been trusted (still a draft, checked by automation only, or confirmed by a
> named person). It opens the source for exact values, and records what it
> could not answer so the gap gets filled. The same docent serves a person at a
> prompt, an agent reading this file, or a chatbot that can load a skill.
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt`
> says how to weigh it.

## Documentation Website

[https://lmodel.github.io/datatype](https://lmodel.github.io/datatype)

## What it models

The schema renders the [Datatype Ontology](http://linked.data.gov.au/def/datatype) ("Datatypes"), which Simon Cox of CSIRO wrote and the Australian Government Linked Data Working Group (AGLDWG) publishes at [AGLDWG/datatype-ont](https://github.com/AGLDWG/datatype-ont). The pinned edition is the ontology of 3 October 2019, its `dcterms:modified` date, at commit `dd8f24120cd5` of the `master` branch. The ontology states no version number, so the schema header's `version` is that date.

Each class wraps one value, for use as an observation result or as the range of another schema's slot:

* `Text`, `Boolean` and `Count`: one string, true-or-false or integer `value`.
* `Concept`: a classifier from a controlled vocabulary, its IRI in `rdf_value` and its vocabulary's IRI in `vocabulary`.
* `QuantitativeMeasure`: a decimal `value` with its `unit` and an optional `uncertainty`.
* `QuantitativeRange`: a `min` and a `max` with their `unit` and an optional `uncertainty`.
* `Percent` and `PercentRange`: a measure and a range whose unit is QUDT's PERCENT, `http://qudt.org/vocab/unit/PERCENT`.

Each class and property keeps the ontology's local name and its IRI under `data:` (`http://linked.data.gov.au/def/datatype/`). `rdf_value` is RDF's own `rdf:value`, which the ontology uses for a `Concept`. `upstream/` holds the ontology's Turtle file and licence at the pinned commit, and `tests/test_upstream.py` holds the schema to that file's classes, properties, ranges and restrictions. A weekly workflow compares the copy with `master` and opens an issue when the ontology, its licence or its namespace moves.

```yaml
# A QuantitativeMeasure: a height of 12.5 metres, give or take 0.25.
value: 12.5
unit: http://qudt.org/vocab/unit/M
uncertainty: 0.25
```

## Influences

None beyond the Datatype Ontology: the schema renders one publication, and its release asset and governance files follow [lmodel/slsa](https://github.com/lmodel/slsa).

## Mappings

None. The ontology states no alignment to another vocabulary, so the schema carries no mapping. Its one link outward is that `value`, `min`, `max` and `uncertainty` are sub-properties of `rdf:value`, which the schema states with `is_a`.

## Not modelled here

* Properties a class's restrictions do not name. OWL leaves each class open to them, but LinkML's classes are closed, so a `standard` on a `QuantitativeMeasure` is not valid here.
* What an IRI names. The ontology says a `Concept`'s value is a `skos:Concept`, and a vocabulary is a SKOS scheme, a SKOS collection or an OWL ontology. No validator can check that of an IRI.
* The ontology's RDF/XML, JSON-LD and HTML forms, which hold the same terms as the Turtle file.
* Rules the ontology does not state: the validator accepts a percent above 100, a negative uncertainty and a range whose `min` is above its `max`.

## Repository Structure

* [docs/](docs/): the website's pages, with the generated schema pages in [elements/](docs/elements/)
* [examples/](examples/): usage examples
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the upstream watch
* [src/datatype/schema/](src/datatype/schema): the LinkML schema, `datatype.yaml` (edit this)
* [src/datatype/datamodel/](src/datatype/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/](tests/data) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [upstream/](upstream/): the ontology's Turtle file and licence at the pinned commit (do not edit them)
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle, in the Linked Open Knowledge Format (LOKF). Its domain schema is `.lokf/datatype.yaml`, which `lokf adapt` writes from `src/datatype/schema/datatype.yaml`. Edit the source, never the copy. A release carries the copy as `schema-<tag>-datatype.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

`just lokf-adapt` rewrites the copy, and `just lokf-adapt-check` says when it is stale. No class is a concept type, so the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins gains nothing from this copy, and no concept names one of its classes as its `type`. Every class is a value class to import: a host's own concept class takes one as the range of a slot, such as a `height` that is a `QuantitativeMeasure`.

LOKF defines `Concept` and `unit`, so the copy renames them `DatatypeConcept` and `datatype_unit`, keeping the ontology's IRIs. Data written for the copy uses those names; data written for the schema uses the ontology's.

A host imports the copy beside LOKF's schema, `lokf.yaml`, and beside other adapt copies. LinkML merges them into one namespace, where the last definition of a name wins silently. No class, enum or type of the copy shares a name with LOKF's or with the thirteen released lmodel copies in `tests/neighbours/`. The copy shares one key, `value`, with six of them (attack, in-toto, oscal, slsa, spdx and stix), each under its own IRI. In a composite with one of them, one copy's `value` projects under the other's IRI. `tests/test_schema_rules.py` lists that key and fails on a new shared name. Do not import this copy beside any of those six until `lokf adapt` can rename what a neighbour defines ([lokf issue 169](https://github.com/nicholsn/lokf/issues/169), `--beside`).

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)).

The knowledge bundle in `.lokf/knowledge/` is under the Creative Commons Attribution 4.0 International licence (CC BY 4.0), as its `index.md` declares.

The ontology states CC0 1.0 as its `dcterms:license`, and the repository it is published from carries a CC BY 4.0 licence, added later. This repository follows the stricter of the two: [NOTICE](NOTICE) attributes the ontology to Simon Cox, CSIRO and the AGLDWG, names the licence and says what was changed. Each description in the schema is the ontology's `skos:definition` of the term.

This is not an official AGLDWG or CSIRO project, and its use implies no endorsement by either.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
