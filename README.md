<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# datatype

AGLDWG Datatype Ontology (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/datatype](https://lmodel.github.io/datatype)

## What it models

The schema renders the [Datatype Ontology](http://linked.data.gov.au/def/datatype) ("Datatypes"), which Simon Cox of CSIRO wrote and the Australian Government Linked Data Working Group (AGLDWG) publishes at [AGLDWG/datatype-ont](https://github.com/AGLDWG/datatype-ont). The pinned edition is the ontology of 3 October 2019 at commit `dd8f24120cd5`. The ontology states no version number, so the schema header's `version` is that date.

Each class wraps one value, such as a text, a count, a classifier or a measure with its unit, for use as an observation result or as the range of another schema's slot. Each class and property keeps its IRI under `data:` (`http://linked.data.gov.au/def/datatype/`).

```yaml
# A QuantitativeMeasure: a height of 12.5 metres, give or take 0.25.
value: 12.5
unit: http://qudt.org/vocab/unit/M
uncertainty: 0.25
```

`upstream/` holds the ontology's Turtle file and licence at the pinned commit, and `tests/test_upstream.py` holds the schema to it. A weekly workflow opens an issue when the ontology, its licence or its namespace moves.

## Mappings

None: the ontology states no alignment to another vocabulary. `value`, `min`, `max` and `uncertainty` are sub-properties of `rdf:value`, which the schema states with `is_a`.

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

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema, `.lokf/datatype.yaml`, is the copy `just lokf-adapt` writes from `src/datatype/schema/datatype.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as `schema-<tag>-datatype.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

No class is a concept type, so the *Known LOKF types* setting gains nothing from this copy. A host's own concept class takes a value class as the range of a slot, such as a `height` that is a `QuantitativeMeasure`.

LOKF defines `Concept` and `unit`, so the copy renames them `DatatypeConcept` and `datatype_unit`, keeping the ontology's IRIs. The copy shares one key, `value`, with six lmodel copies (attack, in-toto, oscal, slsa, spdx and stix), each under its own IRI, and `tests/test_schema_rules.py` fails on a new shared name. Do not import this copy beside any of those six until `lokf adapt` can rename what a neighbour defines ([lokf #169](https://github.com/nicholsn/lokf/issues/169), `--beside`).

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)), and the knowledge bundle in `.lokf/knowledge/` is under CC BY 4.0.

The ontology states CC0 1.0, and the repository it is published from carries CC BY 4.0. This repository follows the stricter of the two: [NOTICE](NOTICE) gives the attribution and says what was changed. This is not an official AGLDWG or CSIRO project, and its use implies no endorsement by either.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
