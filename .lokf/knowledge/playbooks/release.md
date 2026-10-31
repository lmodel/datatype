---
type: Playbook
id: https://w3id.org/lmodel/datatype/knowledge/playbooks/release
genre: how-to
title: Cut a release
description: "How a release is made: Conventional Commits on `main`, an `## [Unreleased]` changelog section, the `v0.0.0` baseline tag that keeps the first release at 0.1.0, and `semantic-release.yml`, which tags the release and dispatches Knowledge Release to attach `schema-<tag>-datatype.yaml` once `KNOWLEDGE_RELEASE_ENABLED` is true."
resource: CONTRIBUTING.md
sources:
  - id: contributing
    resource: CONTRIBUTING.md
    title: Releasing (maintainers)
  - id: releaserc
    resource: .releaserc.json
    title: the release rules
  - id: changelog
    resource: CHANGELOG.md
    title: the baseline paragraph
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:41:26Z"
status: draft
---

# Cut a release

1. Write the `## [Unreleased]` section of `CHANGELOG.md` as you go. The release job refuses an empty one.[^contributing]
2. Type each commit as Conventional Commits say. Only `feat:`, `fix:`, `security:` and a breaking change make a release. `.releaserc.json` makes a breaking change a minor release below 1.0.0.[^releaserc]
3. Before the first releasing merge, push the signed `v0.0.0` tag on `main`, so that the first release is 0.1.0.[^changelog]
4. Merge the pull request. `semantic-release.yml` promotes the changelog section, tags `vX.Y.Z`, publishes the GitHub release, and dispatches Knowledge Release once `KNOWLEDGE_RELEASE_ENABLED` is `true`. Knowledge Release attaches the bundle and `schema-<tag>-datatype.yaml`.[^contributing]

[^contributing]: CONTRIBUTING.md, Releasing (maintainers)
[^releaserc]: .releaserc.json, the release rules
[^changelog]: CHANGELOG.md, the baseline paragraph
