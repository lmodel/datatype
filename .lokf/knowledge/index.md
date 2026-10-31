---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/datatype/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: datatype Knowledge Bundle
description: AGLDWG Datatype Ontology (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/datatype/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# datatype Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for datatype. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [Documentation site](services/documentation-site.md) - The Astro Starlight site in `website/`, for <https://lmodel.github.io/datatype>: the README as its home page, the pages of `docs/`, a page per schema element, a page per concept of this bundle with its trust label, the bundle's exports, and redirects from the retired mkdocs site's pages, built and published by Knowledge website.

# Datasets

* [Datatype LinkML schema](datasets/datatype-linkml-schema.md) - The LinkML schema `src/datatype/schema/datatype.yaml`: the Datatype Ontology's eight classes and seven properties, and `rdf_value` for RDF's `rdf:value`, each with the ontology's local name and IRI under `data:`, at the ontology's edition of 2019-10-03.
* [Copy of the Datatype Ontology](datasets/ontology-copy.md) - `upstream/`: the ontology's Turtle file `rdf/datatype.ttl` and the repository's `LICENSE`, copied from AGLDWG/datatype-ont at commit `dd8f24120cd5` and pinned by git object hash. The schema's tests read the copy, and the upstream watch checks it.
* [Generated artefacts](datasets/generated-artefacts.md) - What the LinkML generators write from the schema: `project/` (JSON Schema, OWL, SHACL, ShEx, JSON-LD, GraphQL, protobuf, SQL, TypeScript, Excel, a prefix map and eight Java classes), the Python dataclasses and Pydantic models in `src/datatype/datamodel/`, and `docs/schema/datatype.yaml`. None is edited by hand.
* [Test data and tests](datasets/test-data.md) - The examples under `tests/data/` (14 valid examples and 21 counter-examples the validator rejects) and the four test files under `tests/` that hold the examples, the ontology copy, the adapt copy and the upstream watch.
* [The adapt copy (.lokf/datatype.yaml)](datasets/lokf-adapt-copy.md) - `.lokf/datatype.yaml`, the copy `lokf adapt` writes from the schema for knowledge bundles: rooted on no class, with `Concept` renamed `DatatypeConcept` and `unit` renamed `datatype_unit`, keeping their IRIs. A release attaches it as `schema-<tag>-datatype.yaml`.

# References

* [The Datatype Ontology](references/datatype-ontology.md) - The Datatype Ontology ("Datatypes"), <http://linked.data.gov.au/def/datatype>, by Simon J.D. Cox of CSIRO, published by the Australian Government Linked Data Working Group (AGLDWG) at AGLDWG/datatype-ont. It was last changed on 2019-10-03, states no version number, and is licensed CC0 1.0 in its own metadata and CC BY 4.0 in its repository.

# Glossary

* [Text](glossary/text.md) - The Datatype Ontology's `data:Text`: class to encapsulate a textual value. A `Text` holds exactly one `value`, a string.
* [Boolean](glossary/boolean.md) - The Datatype Ontology's `data:Boolean`: class to encapsulate a true-or-false value. A `Boolean` holds exactly one `value`, true or false.
* [Count](glossary/count.md) - The Datatype Ontology's `data:Count`: class to encapsulate an integer value. A `Count` holds exactly one `value`, an integer, and at most one `uncertainty`.
* [Quantitative Measure](glossary/quantitative-measure.md) - The Datatype Ontology's `data:QuantitativeMeasure`: class to encapsulate a quantitative measure value. A `QuantitativeMeasure` holds exactly one `value`, a decimal, exactly one `unit`, given by its IRI, and at most one `uncertainty`.
* [Quantitative Range](glossary/quantitative-range.md) - The Datatype Ontology's `data:QuantitativeRange`: class to encapsulate a quantitative range. A `QuantitativeRange` holds exactly one `min` and one `max`, decimals, exactly one `unit` and at most one `uncertainty`.
* [Percent](glossary/percent.md) - The Datatype Ontology's `data:Percent`: class to encapsulate a quantitative measure expressed as a percent value. A `Percent` is a `QuantitativeMeasure` whose unit is QUDT's PERCENT, `http://qudt.org/vocab/unit/PERCENT`.
* [Percent range](glossary/percent-range.md) - The Datatype Ontology's `data:PercentRange`: class to encapsulate a quantitative range expressed as in percent values. A `PercentRange` is a `QuantitativeRange` whose unit is QUDT's PERCENT.
* [Concept (data:Concept)](glossary/datatype-concept.md) - The Datatype Ontology's `data:Concept`: class to encapsulate a classifier, usually a values from a controlled vocabulary. A `Concept` holds exactly one concept by its IRI in `rdf_value`, RDF's `rdf:value`, and exactly one `vocabulary`, the IRI of the vocabulary it comes from. The adapt copy names the class `DatatypeConcept`, since LOKF defines `Concept`.
* [Value class](glossary/value-class.md) - In this repository, a class whose instances are values a knowledge concept holds, such as a measure or a range, and never concepts themselves. Every class of the Datatype Ontology is one, so a host imports them as the ranges of its own concept classes' slots.

# Explanations

* [Scope, influences and mappings](explanations/scope-and-influences.md) - What the schema models (the Datatype Ontology at its 2019-10-03 edition), what it leaves out (properties a class's restrictions do not name, what an IRI names, the ontology's other serialisations), its one-line influences, and why it carries no mapping.
* [Element names and IRIs](explanations/element-names.md) - Why each class and slot keeps the Datatype Ontology's local name and IRI under `data:`, why `rdf_value` renders RDF's `rdf:value`, what the adapt copy renames, and the key `value` it shares with six neighbours.
* [How the schema departs from OWL](explanations/departures-from-owl.md) - Where the LinkML schema differs from the OWL ontology it renders: closed classes, IRIs in place of individuals, a pattern for the fixed PERCENT unit, and no bound or order on any value.

# Playbooks

* [Regenerate and test](playbooks/regenerate-and-test.md) - The steps after a schema edit: `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt`, then `just test`, committing the regenerated files and `.lokf/datatype.yaml` with the change.
* [Cut a release](playbooks/release.md) - How a release is made: Conventional Commits on `main`, an `## [Unreleased]` changelog section, the `v0.0.0` baseline tag that keeps the first release at 0.1.0, and `semantic-release.yml`, which tags the release and dispatches Knowledge Release to attach `schema-<tag>-datatype.yaml` once `KNOWLEDGE_RELEASE_ENABLED` is true.
* [Update the upstream pins](playbooks/update-upstream-pins.md) - What to do when the upstream watch opens an issue: a new commit, tag or `dcterms:modified` date on AGLDWG/datatype-ont, a changed or dropped file, a changed licence, a namespace that redirects elsewhere, or a check that could not finish; and how to move the copy, the pins and the schema header together.
* [Validate data](playbooks/validate-data.md) - How to check a file of datatype values: `linkml-validate -s src/datatype/schema/datatype.yaml -C <Class>`, before loading it into the generated dataclasses or Pydantic models, which check less.
* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location and external page this bundle derives concepts from, the concepts each yields, how to re-check each on a refresh run, and the paths left out on purpose.

# Policies

* [AI covenant](policies/ai-covenant.md) - The repository's rules for work done with artificial intelligence (AI): you own what you submit; an element says what the Datatype Ontology says and cites its triple; a rule of this project's own is marked; no mapping is guessed; the ontology copy is never edited; and every element keeps the ontology's IRI.
* [Licence and attribution](policies/license-and-attribution.md) - The licences: Apache-2.0 for the schema and the code, CC BY 4.0 for the knowledge bundle, and for the Datatype Ontology CC0 1.0 in its own metadata and CC BY 4.0 in its repository, of which NOTICE follows the stricter with an attribution to Simon Cox, CSIRO and the AGLDWG.
* [Security policy](policies/security-policy.md) - How to report a vulnerability (GitHub's private vulnerability reporting), which release receives fixes (the latest), what executes in the repository and what holds each surface, the ruleset on `main`, and the two repository settings that are not yet in force.

# Workflows

* [Build and test (main.yaml)](workflows/main.md) - The Build and test workflow, `.github/workflows/main.yaml`: on a push to main and on every pull request, its test job runs `just test` on Python 3.10 to 3.14, and on 3.13 also `just lint` and `just lokf-adapt-check`, the check that `.lokf/datatype.yaml` is current.
* [Lint & docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - The Lint & docs workflow, `.github/workflows/lint-and-docs.yaml`: on a push to main, every pull request, a Monday 06:00 UTC schedule and by hand, four jobs run ShellCheck, actionlint, the word budgets of CONTRIBUTING.md (1000) and SECURITY.md (900), and markdownlint, lychee and codespell over the Markdown.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The Upstream watch workflow, `.github/workflows/upstream-watch.yaml`: every Monday at 07:00 UTC and by hand, its datatype-copy job runs `scripts/check_upstream_release.py` against AGLDWG/datatype-ont and the ontology's namespace, and on a finding opens or updates the issue titled Upstream watch: the Datatype Ontology has changed.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The Semantic release workflow, `.github/workflows/semantic-release.yml`: on a pull request into main, its plan job checks that the commits, the changelog and the title would release; on a push to main, its release job in the release Environment tags vX.Y.Z, publishes the GitHub release and dispatches Knowledge Release.
* [Knowledge Librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The Knowledge Librarian workflow, `.github/workflows/knowledge-librarian.yaml`: every Monday at 05:00 UTC and by hand, once `KNOWLEDGE_LIBRARIAN_ENABLED` is true, it runs an agent with the ktl-librarian skill (pinned by `TRUST_LADDER_SKILLS_REF` at v0.59.0) in a read-only job and opens a review pull request from a separate job that runs no agent.
* [Knowledge Registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The Knowledge Registrar workflow, `.github/workflows/knowledge-registrar.yaml`: the gate on the knowledge bundle, run on pull requests that touch `.lokf/` or `knowledge_bundle/`, every Monday at 06:00 UTC and by hand; it validates the bundle and its relation targets against the domain schema, runs the conventions script, and checks that each new confirmation by a person is backed by an approval or a signed commit.
* [Knowledge Release (knowledge-release.yaml)](workflows/knowledge-release.md) - The Knowledge Release workflow, `.github/workflows/knowledge-release.yaml`: dispatched with a release's tag, or started by a published release once `KNOWLEDGE_RELEASE_ENABLED` is true, it attaches the bundle zip, the domain schema as `schema-<tag>-datatype.yaml` with its checksum, and the Copilot skills to the release, when the bundle or the schema changed or `force` is set.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The Knowledge sync workflow, `.github/workflows/knowledge-sync.yaml`: every Monday at 04:10 UTC and by hand, it moves the sidecar's copies and the skills pin to the newest Knowledge Trust Ladder release through one pull request, opened with the `KNOWLEDGE_SYNC_TOKEN` secret, and holds the workflow changes for a person to approve.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The Knowledge website workflow, `.github/workflows/knowledge-website.yaml`: on pushes and pull requests that touch the site's sources, every Monday at 05:23 UTC and by hand, its build job builds `website/` and checks its links read-only, and its deploy job publishes the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is true.
