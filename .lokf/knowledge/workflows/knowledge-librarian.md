---
type: Service
id: https://w3id.org/lmodel/datatype/knowledge/workflows/knowledge-librarian
genre: reference
title: Knowledge Librarian (knowledge-librarian.yaml)
description: "The Knowledge Librarian workflow, `.github/workflows/knowledge-librarian.yaml`: every Monday at 05:00 UTC and by hand, once `KNOWLEDGE_LIBRARIAN_ENABLED` is true, it runs an agent with the ktl-librarian skill (pinned by `TRUST_LADDER_SKILLS_REF` at v0.59.0) in a read-only job and opens a review pull request from a separate job that runs no agent."
resource: .github/workflows/knowledge-librarian.yaml
sources:
  - id: knowledge-librarian.yaml
    resource: .github/workflows/knowledge-librarian.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:41:26Z"
status: draft
---

# Knowledge Librarian (knowledge-librarian.yaml)

`.github/workflows/knowledge-librarian.yaml` is the workflow named "Knowledge Librarian". It is a copy of the ktl-sidecar template. It runs every Monday at 05:00 UTC and by hand, and does nothing until the repository variable `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`. Its `earlier` job reads what became of the pull requests it opened before. Its `refresh` job, in the `knowledge-librarian` Environment and with a read-only checkout, installs the ktl-librarian skill at `TRUST_LADDER_SKILLS_REF`, `v0.59.0`, runs the agent, and hands on a patch. Its `publish` job runs no agent: it applies the patch and opens the review pull request.[^knowledge-librarian.yaml]

[^knowledge-librarian.yaml]: .github/workflows/knowledge-librarian.yaml, the header comment, the on key and the jobs
