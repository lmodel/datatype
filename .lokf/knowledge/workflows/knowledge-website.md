---
type: Service
id: https://w3id.org/lmodel/datatype/knowledge/workflows/knowledge-website
genre: reference
title: Knowledge website (knowledge-website.yaml)
description: "The Knowledge website workflow, `.github/workflows/knowledge-website.yaml`: on pushes and pull requests that touch the site's sources, every Monday at 05:23 UTC and by hand, its build job builds `website/` and checks its links read-only, and its deploy job publishes the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is true."
resource: .github/workflows/knowledge-website.yaml
sources:
  - id: knowledge-website.yaml
    resource: .github/workflows/knowledge-website.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-11-15T03:03:20Z"
status: draft
---

# Knowledge website (knowledge-website.yaml)

`.github/workflows/knowledge-website.yaml` is the workflow named "Knowledge website". It is a copy of the ktl-website template. It runs every Monday at 05:23 UTC and by hand. It also runs on a push or a pull request that touches `website/`, `ktl-website/`, `.lokf/`, `knowledge_bundle/`, the README, `docs/`, `.assets/`, the changelog, `.linkml/`, a schema under `src/*/schema/`, this workflow or the knowledge federation workflow.[^knowledge-website.yaml]

Its `build` job runs with `contents: read`, and a push builds on the default branch only. The job checks out the whole history, sets up uv and runs `website/scripts/build.sh`. That script runs `lokf export` and `gen-doc`, builds the site with Hugo and Pagefind, cleans its raw HTML and checks its links. The job then uploads `website/dist` as the Pages artifact.[^knowledge-website.yaml]

Its `deploy` job holds `pages: write` and `id-token: write` in the `github-pages` Environment. It runs for the default branch only, once the repository variable `KNOWLEDGE_WEBSITE_ENABLED` is `true`.[^knowledge-website.yaml]

[^knowledge-website.yaml]: .github/workflows/knowledge-website.yaml, the header comment, the on key and the jobs
