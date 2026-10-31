---
type: Dataset
id: https://w3id.org/lmodel/datatype/knowledge/datasets/test-data
genre: reference
title: Test data and tests
description: The examples under `tests/data/` (14 valid examples and 21 counter-examples the validator rejects) and the four test files under `tests/` that hold the examples, the ontology copy, the adapt copy and the upstream watch.
resource: tests
derivedFrom:
  - https://w3id.org/lmodel/datatype/knowledge/datasets/datatype-linkml-schema
sources:
  - id: data
    resource: tests/data
    title: the valid and invalid folders
  - id: test_data
    resource: tests
    title: the four test files
generated:
  by: process:ktl-librarian
  at: "2026-10-31T18:04:29Z"
status: draft
---

# Test data and tests

`tests/data/valid/` holds 14 examples, at least one per class, and `tests/data/invalid/` holds 21 counter-examples, at least one per class. Each file is named after its class, and each counter-example's first line, `# Fails at: <JSON pointer>`, names the one place it fails.[^data]

`tests/test_data.py` holds the examples to the validator and to the committed JSON Schema. It also makes counter-examples from each slot of each valid example, a list, and a word where the slot takes a number or a truth value, and checks that each fails at that slot. `tests/test_upstream.py` holds the schema to the ontology copy, and the schema header to the watch's pins. `tests/test_schema_rules.py` holds the adapt copy apart from LOKF and from the thirteen released copies in `tests/neighbours/`. `tests/test_watch.py` runs the upstream watch against stubbed answers.[^test_data]

[^data]: tests/data, the valid and invalid folders
[^test_data]: tests, the four test files
