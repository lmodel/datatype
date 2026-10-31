---
type: Policy
id: https://w3id.org/lmodel/datatype/knowledge/policies/security-policy
genre: reference
title: Security policy
description: How to report a vulnerability (GitHub's private vulnerability reporting), which release receives fixes (the latest), what executes in the repository and what holds each surface, the ruleset on `main`, and the two repository settings that are not yet in force.
resource: SECURITY.md
sources:
  - id: security
    resource: SECURITY.md
    title: every section
  - id: dependabot
    resource: .github/dependabot.yml
    title: the five update entries
generated:
  by: process:ktl-librarian
  at: "2026-10-31T18:02:18Z"
status: draft
---

# Security policy

`SECURITY.md` asks for a vulnerability to be reported through GitHub's private vulnerability reporting, not in a public issue. It says that one person maintains the repository, so a first reply takes days and there is no bounty. It also says that only the latest release receives fixes.[^security]

The repository releases the schema and the Python models generated from it. Nothing is published to PyPI. A release carries three assets, each with its `.sha256` and an attestation: the adapt copy, the bundle zip and a Copilot skill zip. The upstream watch reads the GitHub API's listings of AGLDWG/datatype-ont. It reads the ontology's Turtle file only when `master` changes it, and checks that file against the hash the listing gives. It sends its token to api.github.com alone. The policy's table names each workflow and what holds it.[^security]

Every workflow declares `permissions: {}` at the top, pins its actions to commit hashes and runs harden-runner in audit mode. Dependabot keeps the action pins, the package's lock, the sidecar's lock, the website's npm packages and the release tools' npm lock current, each monthly.[^dependabot] A ruleset on `main` blocks deletion and force-pushes and keeps the history linear. Two settings are not yet in force: required reviewers on the `release` Environment, and secret scanning with push protection.[^security]

[^security]: SECURITY.md, every section
[^dependabot]: .github/dependabot.yml, the five update entries
