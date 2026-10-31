---
type: Playbook
id: https://w3id.org/lmodel/datatype/knowledge/playbooks/knowledge-sources
genre: reference
title: Knowledge sources map
description: "The librarian's scrape map: every repository location and external page this bundle derives concepts from, the concepts each yields, how to re-check each on a refresh run, and the paths left out on purpose."
resource: .
sources:
  - resource: README.md
  - resource: docs/about.md
  - resource: docs/index.md
  - resource: src/datatype/schema
  - resource: src/datatype/datamodel
  - resource: upstream
  - resource: project.justfile
  - resource: .lokf/datatype.yaml
  - resource: .lokf/justfile
  - resource: .lokf/pyproject.toml
  - resource: NOTICE
  - resource: LICENSE
  - resource: scripts/check_upstream_release.py
  - resource: .github/scripts
  - resource: .github/workflows
  - resource: .github/dependabot.yml
  - resource: .github/release
  - resource: justfile
  - resource: .linkml/generators.yaml
  - resource: .linkmllint.yaml
  - resource: .pre-commit-config.yaml
  - resource: project
  - resource: docs/schema
  - resource: tests
  - resource: CONTRIBUTING.md
  - resource: .releaserc.json
  - resource: CHANGELOG.md
  - resource: website
  - resource: SECURITY.md
  - resource: AI_COVENANT.md
exclusions:
  - resource: .github/ISSUE_TEMPLATE
    reason: Issue forms, which are governance text and state nothing about the schema.
  - resource: .github/pull_request_template.md
    reason: The pull request checklist, which repeats CONTRIBUTING.md.
  - resource: .github/PULL_REQUEST_TEMPLATE
    reason: The knowledge sync's pull request checklist, a copy of the ktl-sidecar template.
  - resource: CODE_OF_CONDUCT.md
    reason: The Contributor Covenant, governance text with nothing about the schema.
  - resource: uv.lock
    reason: The package's lock file, tooling that pins versions.
  - resource: pyproject.toml
    reason: Package metadata and spell checkers' settings; the changelog states the Python project's name.
  - resource: .gitignore
    reason: "Tooling: the files git ignores."
  - resource: .editorconfig
    reason: "Tooling: editor settings."
  - resource: .yamllint.yaml
    reason: "Tooling: the YAML linter's settings."
  - resource: .markdownlint-cli2.jsonc
    reason: "Tooling: the Markdown linter's settings."
  - resource: lychee.toml
    reason: "Tooling: the link checker's settings."
  - resource: config.public.mk
    reason: "Tooling: the variables the justfile loads."
  - resource: .copier-answers.yml
    reason: The copier template's answers, which `just update` reads.
  - resource: src/README.md
    reason: Text from the project template.
  - resource: docs/templates-linkml
    reason: The template's placeholders for gen-doc, not pages.
  - resource: docs/elements
    reason: gen-doc's output folder, which git ignores but for its placeholder.
  - resource: examples/README.md
    reason: Text from the project template about generated example output.
  - resource: src/datatype/__init__.py
    reason: Package plumbing.
  - resource: src/datatype/_version.py
    reason: Package plumbing.
  - resource: tests/__init__.py
    reason: Test plumbing.
  - resource: llms.txt
    reason: The pointer that sends agents to this bundle.
  - resource: knowledge_bundle
    reason: The link to .lokf/knowledge, the bundle itself.
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:41:26Z"
status: draft
---

# Knowledge sources map

This map lists where the bundle's concepts come from, so that a refresh run knows what to re-read.

| Source | Yields | Re-check |
| --- | --- | --- |
| `src/datatype/schema/datatype.yaml`, `.linkmllint.yaml` | the schema dataset and the glossary terms | read the classes and slots again |
| `upstream/` | the ontology copy and the ontology reference | `scripts/check_upstream_release.py` and `tests/test_upstream.py` |
| `project/`, `src/datatype/datamodel/`, `docs/schema/`, `justfile`, `.linkml/generators.yaml`, `.pre-commit-config.yaml` | the generated artefacts | rerun `just gen-project` and `just gen-doc` |
| `project.justfile`, `.lokf/datatype.yaml`, `.lokf/justfile`, `.lokf/pyproject.toml` | the adapt copy and the value class term | `just lokf-adapt-check` |
| `tests/` | the test data | `just test` |
| `README.md`, `docs/` | the explanations and the data validation playbook | read the sections again |
| `CONTRIBUTING.md`, `CHANGELOG.md`, `.releaserc.json`, `.github/release/` | the playbooks | read the checklists again |
| `AI_COVENANT.md`, `NOTICE`, `LICENSE`, `SECURITY.md`, `.github/dependabot.yml` | the policies | read the sections again |
| `.github/workflows/`, `.github/scripts/`, `scripts/check_upstream_release.py` | the workflow concepts and the upstream playbook | read each header comment, `on` key and jobs |
| `website/` | the documentation site | `npm run build` in `website/` |
| <http://linked.data.gov.au/def/datatype> | the ontology reference | the upstream watch's namespace check |

The exclusions list the tracked paths the map leaves out, each with its reason.
