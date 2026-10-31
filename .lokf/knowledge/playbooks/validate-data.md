---
type: Playbook
id: https://w3id.org/lmodel/datatype/knowledge/playbooks/validate-data
genre: how-to
title: Validate data
description: "How to check a file of datatype values: `linkml-validate -s src/datatype/schema/datatype.yaml -C <Class>`, before loading it into the generated dataclasses or Pydantic models, which check less."
resource: docs/index.md
sources:
  - id: index
    resource: docs/index.md
    title: Validating data
generated:
  by: process:ktl-librarian
  at: "2026-10-31T18:02:18Z"
status: draft
---

# Validate data

1. Run `linkml-validate -s src/datatype/schema/datatype.yaml -C QuantitativeMeasure measure.yaml`, naming the class the file holds. It checks the file against the JSON Schema generated from the schema.[^index]
2. Only then load the file into a model in `src/datatype/datamodel/`. The dataclasses check no pattern, and the Pydantic models read a word such as "yes" as a true `Boolean`.[^index]

[^index]: docs/index.md, Validating data
