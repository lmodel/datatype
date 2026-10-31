# Change Log

## 2026-10-31

* **Changed**: Security policy, which now names the four locks and the action pins Dependabot keeps current, as `.github/dependabot.yml` lists them.
* **Added**: Datatype LinkML schema, from `src/datatype/schema/datatype.yaml`.
* **Added**: Copy of the Datatype Ontology, from `upstream`.
* **Added**: Generated artefacts, from `project`.
* **Added**: Test data and tests, from `tests`.
* **Added**: The adapt copy (.lokf/datatype.yaml), from `.lokf/datatype.yaml`.
* **Added**: The Datatype Ontology, from <http://linked.data.gov.au/def/datatype>.
* **Added**: Text, from `src/datatype/schema/datatype.yaml`.
* **Added**: Boolean, from `src/datatype/schema/datatype.yaml`.
* **Added**: Count, from `src/datatype/schema/datatype.yaml`.
* **Added**: Quantitative Measure, from `src/datatype/schema/datatype.yaml`.
* **Added**: Quantitative Range, from `src/datatype/schema/datatype.yaml`.
* **Added**: Percent, from `src/datatype/schema/datatype.yaml`.
* **Added**: Percent range, from `src/datatype/schema/datatype.yaml`.
* **Added**: Concept (data:Concept), from `src/datatype/schema/datatype.yaml`.
* **Added**: Value class, from `project.justfile`.
* **Added**: Scope, influences and mappings, from `README.md`.
* **Added**: Element names and IRIs, from `docs/about.md`.
* **Added**: How the schema departs from OWL, from `docs/about.md`.
* **Added**: Regenerate and test, from `CONTRIBUTING.md`.
* **Added**: Cut a release, from `CONTRIBUTING.md`.
* **Added**: Update the upstream pins, from `scripts/check_upstream_release.py`.
* **Added**: Validate data, from `docs/index.md`.
* **Added**: AI covenant, from `AI_COVENANT.md`.
* **Added**: Licence and attribution, from `NOTICE`.
* **Added**: Security policy, from `SECURITY.md`.
* **Added**: Documentation site, from `website`.
* **Added**: Build and test (main.yaml), from `.github/workflows/main.yaml`.
* **Added**: Lint & docs (lint-and-docs.yaml), from `.github/workflows/lint-and-docs.yaml`.
* **Added**: Upstream watch (upstream-watch.yaml), from `.github/workflows/upstream-watch.yaml`.
* **Added**: Semantic release (semantic-release.yml), from `.github/workflows/semantic-release.yml`.
* **Added**: Knowledge Librarian (knowledge-librarian.yaml), from `.github/workflows/knowledge-librarian.yaml`.
* **Added**: Knowledge Registrar (knowledge-registrar.yaml), from `.github/workflows/knowledge-registrar.yaml`.
* **Added**: Knowledge Release (knowledge-release.yaml), from `.github/workflows/knowledge-release.yaml`.
* **Added**: Knowledge sync (knowledge-sync.yaml), from `.github/workflows/knowledge-sync.yaml`.
* **Added**: Knowledge website (knowledge-website.yaml), from `.github/workflows/knowledge-website.yaml`.
* **Added**: Knowledge sources map, the librarian's scrape map, from the repository's tree.
* **Removal**: the sidecar's two example services, which the bootstrap's concepts replace.
* **Initialization**: Scaffolded the LOKF bundle for datatype with placeholder
  services. Real concepts to follow.
