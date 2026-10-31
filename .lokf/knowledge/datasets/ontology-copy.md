---
type: Dataset
id: https://w3id.org/lmodel/datatype/knowledge/datasets/ontology-copy
genre: reference
title: Copy of the Datatype Ontology
description: "`upstream/`: the ontology's Turtle file `rdf/datatype.ttl` and the repository's `LICENSE`, copied from AGLDWG/datatype-ont at commit `dd8f24120cd5` and pinned by git object hash. The schema's tests read the copy, and the upstream watch checks it."
resource: upstream
derivedFrom:
  - https://w3id.org/lmodel/datatype/knowledge/references/datatype-ontology
sources:
  - id: watch
    resource: scripts/check_upstream_release.py
    title: PINNED_COMMIT and PINNED_BLOBS
  - id: notice
    resource: NOTICE
    title: The Datatype Ontology
  - id: test_upstream
    resource: tests/test_upstream.py
    title: the module docstring and the tests
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:41:26Z"
status: draft
---

# Copy of the Datatype Ontology

`upstream/` holds two files from AGLDWG/datatype-ont: `rdf/datatype.ttl`, the ontology in Turtle, and `LICENSE`, the repository's licence. `scripts/check_upstream_release.py` pins the commit they come from, `dd8f24120cd59f686086f58175de37807c569e18` on `master`, and the git object hash of each file.[^watch]

Each file is identical to its counterpart at that commit, and nothing in the repository changes them.[^notice] `tests/test_upstream.py` checks the hashes offline and holds the schema to the Turtle file's classes, properties, labels, definitions, ranges, super-properties and restrictions.[^test_upstream]

[^watch]: scripts/check_upstream_release.py, PINNED_COMMIT and PINNED_BLOBS
[^notice]: NOTICE, The Datatype Ontology
[^test_upstream]: tests/test_upstream.py, the module docstring and the tests
