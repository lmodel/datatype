---
type: Service
id: https://w3id.org/lmodel/datatype/knowledge/workflows/knowledge-release
genre: reference
title: Knowledge Release (knowledge-release.yaml)
description: "The Knowledge Release workflow, `.github/workflows/knowledge-release.yaml`: dispatched with a release's tag, or started by a published release once `KNOWLEDGE_RELEASE_ENABLED` is true, it attaches the bundle zip, the domain schema as `schema-<tag>-datatype.yaml` with its checksum, and the Copilot skills to the release, when the bundle or the schema changed or `force` is set."
resource: .github/workflows/knowledge-release.yaml
sources:
  - id: knowledge-release.yaml
    resource: .github/workflows/knowledge-release.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:41:26Z"
status: draft
---

# Knowledge Release (knowledge-release.yaml)

`.github/workflows/knowledge-release.yaml` is the workflow named "Knowledge Release". It is a copy of the ktl-sidecar template. It runs when dispatched by hand with a `tag`, and on each published release once the repository variable `KNOWLEDGE_RELEASE_ENABLED` is `true`. Its `pack` job, under a read-only token, validates and packs the bundle zip, the schema copy as `schema-<tag>-datatype.yaml` with its `.sha256`, and one Copilot skill zip per instructions file under `.lokf/m365/`. It skips a release whose bundle and schema match the last one, unless `force` is set. Its `attach` job alone can write: it attaches the assets and their build-provenance attestations to the release.[^knowledge-release.yaml]

[^knowledge-release.yaml]: .github/workflows/knowledge-release.yaml, the header comment, the on key and the jobs
