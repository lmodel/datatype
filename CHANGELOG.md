# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

### Security

- **The sidecar copies and the skills pin are at Knowledge Trust Ladder [v0.70.4](https://github.com/noelmcloughlin/knowledge-trust-ladder/compare/v0.66.0...v0.70.4).** The release changed `.github/workflows/knowledge-registrar.yaml`, `.github/workflows/knowledge-librarian.yaml`, `.github/workflows/knowledge-release.yaml`, `.github/workflows/knowledge-sync.yaml`, `.github/PULL_REQUEST_TEMPLATE/knowledge-sync.md`, `.lokf/scripts/knowledge-conventions.sh`, `.lokf/scripts/knowledge-conventions.py`, `.lokf/scripts/knowledge-preflight.sh`, `.lokf/scripts/knowledge-provenance.sh`, `.lokf/scripts/knowledge-feedback.sh`, `.lokf/scripts/knowledge-apply.py`, `.lokf/scripts/knowledge-report.sh`, `.lokf/scripts/knowledge-sync.sh`, `.lokf/m365/ktl-docent-m365.md`, `.lokf/justfile`, `website/assets/css/site.css`, `website/assets/js/graph.js`, `website/assets/js/site.js`, `website/content/_content.gotmpl`, `website/content/knowledge/_content.gotmpl`, `website/.gitignore`, `website/hugo.toml`, `website/layouts/_markup/render-blockquote.html`, `website/layouts/_markup/render-codeblock-mermaid.html`, `website/layouts/_markup/render-heading.html`, `website/layouts/_markup/render-link.html`, `website/layouts/_partials/gendoc.html`, `website/layouts/_partials/heroes.html`, `website/layouts/_partials/icon.html`, `website/layouts/_partials/markdown-file.html`, `website/layouts/_partials/nav-key.html`, `website/layouts/_partials/route.html`, `website/layouts/_partials/schema-file.html`, `website/layouts/_partials/sidebar.html`, `website/layouts/_partials/tools.html`, `website/layouts/_partials/vendor.html`, `website/layouts/baseof.html`, `website/layouts/health.html`, `website/layouts/home.badge.json`, `website/layouts/home.llms.txt`, `website/layouts/page.atom.xml`, `website/layouts/page.html`, `website/layouts/schema/section.html`, `website/pyproject.toml`, `website/scripts/build.sh`, `website/scripts/clean-html.py`, `website/scripts/prepare.sh`, `website/uv.lock`, `.github/workflows/knowledge-website.yaml`, `website/layouts/_partials/own.html`, `website/layouts/_partials/spec.html`, `website/scripts/check-svg.py`, `website/scripts/lokf-export.py`, `website/scripts/site-values.py`, `website/scripts/uv-env.sh` and `website/scripts/vendor.sh` here.

## [0.2.3] - 2026-11-16

### Fixed

- **Each GitHub release carries its changelog section as its body**: semantic-release asks for the notes again after the changelog commit, and `changelog-release.mjs notes` now answers with the promoted section instead of the empty Unreleased one.

## [0.2.2] - 2026-11-15

### Changed

- **The release tools are in `.release/`**, outside `.github/`, where Dependabot's pull requests for them were refused.

## [0.2.1] - 2026-11-15

### Added

- **`scorecard.yml` publishes this repository's OpenSSF Scorecard.**
- **The README shows the CI, licence, OpenSSF Scorecard and KTL scorecard badges.**
- **`codeql.yml` scans the Python, the JavaScript and the workflows with CodeQL.**

### Changed

- **The knowledge website is built with Hugo from the ktl-website templates**, set by `website/site.toml`, in place of the Astro site.
- **The project requires Python 3.11 or later**, since Python 3.10's support ended in October 2026.

### Security

- **The sidecar copies are at Knowledge Trust Ladder [v0.66.0](https://github.com/noelmcloughlin/knowledge-trust-ladder/blob/v0.66.0/CHANGELOG.md), and `.lokf/pyproject.toml` pins `ktl==0.66.0`**, which the librarian installs its skill from.

## [0.2.0] - 2026-11-07

### Added

- **The schema as RDF Turtle and the merged schema**, in `project/rdf/` and `project/linkml/`, from `just gen-rdf` and `just gen-merged-schema`.

### Changed

- **The bundle's schema files sit in `.lokf/schema/`**: `lokf.yaml` and the `lokf adapt` copy `datatype.yaml`, as KTL v0.62.0 lays them out.

## [0.1.1] - 2026-11-02

### Security

- **The sidecar copies and the skills pin are at Knowledge Trust Ladder [v0.60.0](https://github.com/noelmcloughlin/knowledge-trust-ladder/compare/v0.59.0...v0.60.0).** The release changed `.github/workflows/knowledge-registrar.yaml`, `.github/workflows/knowledge-librarian.yaml`, `.github/workflows/knowledge-release.yaml`, `.github/workflows/knowledge-sync.yaml`, `.lokf/scripts/knowledge-preflight.sh`, `.lokf/.gitignore`, `.lokf/justfile`, `website/package-lock.json`, `website/package.json`, `website/scripts/config.mjs`, `website/scripts/sync.mjs` and `.github/workflows/knowledge-website.yaml` here.

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
