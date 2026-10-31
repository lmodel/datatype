# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

## [0.1.0] - 2026-10-31

### Added

- **A LinkML rendering of the Datatype Ontology of 3 October 2019**, from the Australian Government Linked Data Working Group (AGLDWG). Each class and property keeps the ontology's local name and IRI, and tests hold the schema to a copy of the ontology's Turtle file.
- **`upstream/`, the ontology's Turtle file and licence at commit `dd8f24120cd5`**, and a weekly upstream watch that reports a new commit, tag or `dcterms:modified` date, a changed or dropped file, a changed licence, a moved namespace or a check that could not finish.
- **`.lokf/datatype.yaml`, the schema's `lokf adapt` copy, rooted on no class**, since every class is a value a concept holds. The knowledge release attaches it as `schema-<tag>-datatype.yaml`, and tests hold its names apart from those of the Linked Open Knowledge Format (LOKF) and of thirteen released lmodel copies.
- **An example of each class and a counter-example for each constraint**, held to the validator and to the committed JSON Schema by `just test`.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.59.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.
- **`.github/release/package-lock.json`, which pins semantic-release and every package it pulls in.** The release job installs from it with `npm ci`, and Dependabot keeps it current.

### Changed

- **The schema follows the ontology's own restrictions.** Each class carries only the properties they name, `Concept` holds its concept in `rdf_value` (RDF's `rdf:value`), and a `Percent` or `PercentRange` takes QUDT's PERCENT as its one unit. `min`, `max`, `uncertainty` and `value` are sub-properties of `rdf:value`.
- **The version is the ontology's `dcterms:modified` date, `2019-10-03`,** since the ontology states no version.
- **The Python project's name is `datatype-linkml`.** PyPI publishing stays off.

### Removed

- **The mappings to NCIT, Wikidata, schema.org, STATO, OBCS, UO, QUDT and SKOS, and the seven types of the schema's own.** The ontology states none of the mappings, and the built-in LinkML types take the types' place.
- **The PyPI publishing workflow and the mkdocs site and its preview.** The knowledge website replaces the site.
