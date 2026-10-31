---
type: Playbook
id: https://w3id.org/lmodel/datatype/knowledge/playbooks/update-upstream-pins
genre: how-to
title: Update the upstream pins
description: "What to do when the upstream watch opens an issue: a new commit or tag on AGLDWG/datatype-ont, a changed or dropped file, a changed licence, a namespace that redirects elsewhere, or a check that could not finish; and how to move the copy, the pins and the schema header together."
resource: scripts/check_upstream_release.py
sources:
  - id: workflow
    resource: .github/workflows/upstream-watch.yaml
    title: the schedule and the steps
  - id: watch
    resource: scripts/check_upstream_release.py
    title: the module docstring and the pins
  - id: contributing
    resource: CONTRIBUTING.md
    title: Leave upstream/ as the AGLDWG published it
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:41:26Z"
status: draft
---

# Update the upstream pins

`upstream-watch.yaml` runs `scripts/check_upstream_release.py` every Monday and opens an issue on a finding.[^workflow] The script reports, and exits 1 on:[^watch]

- `master` naming another commit, or the repository gaining a tag;
- a copied file changed or gone at the head of `master`, or a copy that differs from its pins;
- a licence other than CC-BY-4.0, or none;
- the namespace redirecting somewhere else, or not at all;
- a check that could not finish.

To move to a new edition, replace `upstream/` from one commit, then move `PINNED_COMMIT`, `PINNED_BLOBS` and `PINNED_EDITION` in the script and the header's `version` and annotations together, since `tests/test_upstream.py` holds them equal.[^contributing] Then regenerate and test.

[^workflow]: .github/workflows/upstream-watch.yaml, the schedule and the steps
[^watch]: scripts/check_upstream_release.py, the module docstring and the pins
[^contributing]: CONTRIBUTING.md, Leave upstream/ as the AGLDWG published it
