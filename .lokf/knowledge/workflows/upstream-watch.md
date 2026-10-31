---
type: Service
id: https://w3id.org/lmodel/datatype/knowledge/workflows/upstream-watch
genre: reference
title: Upstream watch (upstream-watch.yaml)
description: "The Upstream watch workflow, `.github/workflows/upstream-watch.yaml`: every Monday at 07:00 UTC and by hand, its datatype-copy job runs `scripts/check_upstream_release.py` against AGLDWG/datatype-ont and the ontology's namespace, and on a finding opens or updates the issue titled Upstream watch: the Datatype Ontology has changed."
resource: .github/workflows/upstream-watch.yaml
sources:
  - id: upstream-watch.yaml
    resource: .github/workflows/upstream-watch.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:41:26Z"
status: draft
---

# Upstream watch (upstream-watch.yaml)

`.github/workflows/upstream-watch.yaml` is the workflow named "Upstream watch". It runs every Monday at 07:00 UTC and by hand, since nothing in a pull request can change what it checks. Its one job, `datatype-copy`, reads the checkout, holds `issues: write` and has 10 minutes to finish. It runs `scripts/check_upstream_release.py` on the runner's Python with the workflow's token, and on a finding `.github/scripts/report-issue.sh` opens the issue titled "Upstream watch: the Datatype Ontology has changed" or comments on the open one.[^upstream-watch.yaml]

[^upstream-watch.yaml]: .github/workflows/upstream-watch.yaml, the header comment, the on key and the jobs
