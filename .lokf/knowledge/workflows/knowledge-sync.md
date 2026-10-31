---
type: Service
id: https://w3id.org/lmodel/datatype/knowledge/workflows/knowledge-sync
genre: reference
title: Knowledge sync (knowledge-sync.yaml)
description: "The Knowledge sync workflow, `.github/workflows/knowledge-sync.yaml`: every Monday at 04:10 UTC and by hand, it moves the sidecar's copies and the skills pin to the newest Knowledge Trust Ladder release through one pull request, opened with the `KNOWLEDGE_SYNC_TOKEN` secret, and holds the workflow changes for a person to approve."
resource: .github/workflows/knowledge-sync.yaml
sources:
  - id: knowledge-sync.yaml
    resource: .github/workflows/knowledge-sync.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:41:26Z"
status: draft
---

# Knowledge sync (knowledge-sync.yaml)

`.github/workflows/knowledge-sync.yaml` is the workflow named "Knowledge sync". It is a copy of the ktl-sidecar template. It runs every Monday at 04:10 UTC and by hand, with an optional `tag`. Its `earlier` job reads the pin, the newest release and the last pull request. Its `sync` job writes the copies that differ from that release's templates. Its `publish` job, in the `knowledge-sync` Environment, opens or refreshes one pull request with the `KNOWLEDGE_SYNC_TOKEN` secret. A `review` job holds a change to the workflows in the Environment `KNOWLEDGE_SYNC_REVIEW_ENVIRONMENT` names, and `push-workflows` pushes it once a person approves.[^knowledge-sync.yaml]

[^knowledge-sync.yaml]: .github/workflows/knowledge-sync.yaml, the header comment, the on key and the jobs
