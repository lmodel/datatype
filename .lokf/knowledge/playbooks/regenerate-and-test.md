---
type: Playbook
id: https://w3id.org/lmodel/datatype/knowledge/playbooks/regenerate-and-test
genre: how-to
title: Regenerate and test
description: "The steps after a schema edit: `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt`, then `just test`, committing the regenerated files and `.lokf/datatype.yaml` with the change."
resource: CONTRIBUTING.md
sources:
  - id: contributing
    resource: CONTRIBUTING.md
    title: Before opening a pull request
  - id: justfile
    resource: justfile
    title: the lint and test recipes
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:41:26Z"
status: draft
---

# Regenerate and test

1. Edit `src/datatype/schema/datatype.yaml`, never a generated file.[^contributing]
2. Run `just lint`, which fails on a warning under `.linkmllint.yaml`.[^justfile]
3. Run `just gen-project`, `just gen-doc` and `just lokf-adapt`, and commit what they write.[^contributing]
4. Run `just test`: it generates the project into `tmp/`, runs `pytest` and runs the example runner over `tests/data/valid/` and `tests/data/invalid/`.[^justfile]
5. Add a valid example for a new class and a counter-example for a new constraint, its first line `# Fails at: <pointer>`.[^contributing]

[^contributing]: CONTRIBUTING.md, Before opening a pull request
[^justfile]: justfile, the lint and test recipes
