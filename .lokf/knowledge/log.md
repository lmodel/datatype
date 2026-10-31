# Change Log

## 2026-10-31

* **Prose**: reworded 12 concept bodies in plain English. No fact, link, number or frontmatter changed.
* **Changed**: Test data and tests, which says that the data test makes a word counter-example only for a number or a truth value.
* **Changed**: How the schema departs from OWL, which drops the rule that a range's min is not above its max, since the schema no longer states it.
* **Changed**: Quantitative Range, which drops the rule on min and max that the schema no longer states.
* **Changed**: Validate data, which drops the step that checked a range's min against its max by hand.
* **Changed**: Test data and tests, which drops the counter-example to the min and max rule and names the counter-examples the data test makes from each slot.
* **Changed**: Update the upstream pins, which names the watch's new report of the date and licence a changed Turtle file states.
* **Changed**: Security policy, which says the upstream watch now reads a changed Turtle file, checked against its hash.
* **Prose**: reworded 12 concept bodies in plain English. No fact, link, number or frontmatter changed.
* **Changed**: Percent, which no longer names a bound on its value: the schema dropped the bound of 0 to 100, which the ontology does not state.
* **Changed**: Percent range, which no longer names a bound on its min and max: the schema dropped the bound of 0 to 100, which the ontology does not state.
* **Changed**: Quantitative Range, which now says the ontology does not state the rule that min is not above max.
* **Changed**: How the schema departs from OWL, which drops the percent and uncertainty bounds the schema no longer states and keeps the one rule of the project's own.
* **Changed**: Test data and tests, which now counts 21 counter-examples, since the five for the dropped bounds are gone.
* **Changed**: Validate data, which no longer speaks of bounds, since the schema states none.
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
