---
type: Service
id: https://w3id.org/lmodel/datatype/knowledge/workflows/lint-and-docs
genre: reference
title: Lint & docs (lint-and-docs.yaml)
description: "The Lint & docs workflow, `.github/workflows/lint-and-docs.yaml`: on a push to main, every pull request, a Monday 06:00 UTC schedule and by hand, four jobs run ShellCheck, actionlint, the word budgets of CONTRIBUTING.md (1000) and SECURITY.md (900), and markdownlint, lychee and codespell over the Markdown."
resource: .github/workflows/lint-and-docs.yaml
sources:
  - id: lint-and-docs.yaml
    resource: .github/workflows/lint-and-docs.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:41:26Z"
status: draft
---

# Lint & docs (lint-and-docs.yaml)

`.github/workflows/lint-and-docs.yaml` is the workflow named "Lint & docs". It runs on a push to `main`, on every pull request, every Monday at 06:00 UTC and by hand. Its four jobs run read-only, each within 15 minutes:

- `lint-scripts` runs ShellCheck;
- `lint-workflows` runs actionlint;
- `word-budgets` holds `CONTRIBUTING.md` to 1000 words and `SECURITY.md` to 900;
- `validate-markdown` runs markdownlint, lychee and codespell over every tracked Markdown file.[^lint-and-docs.yaml]

[^lint-and-docs.yaml]: .github/workflows/lint-and-docs.yaml, the header comment, the on key and the jobs
