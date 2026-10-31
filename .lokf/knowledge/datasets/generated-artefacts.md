---
type: Dataset
id: https://w3id.org/lmodel/datatype/knowledge/datasets/generated-artefacts
genre: reference
title: Generated artefacts
description: "What the LinkML generators write from the schema: `project/` (JSON Schema, OWL, SHACL, ShEx, JSON-LD, GraphQL, protobuf, SQL, TypeScript, Excel, a prefix map and eight Java classes), the Python dataclasses and Pydantic models in `src/datatype/datamodel/`, and `docs/schema/datatype.yaml`. None is edited by hand."
resource: project
derivedFrom:
  - https://w3id.org/lmodel/datatype/knowledge/datasets/datatype-linkml-schema
sources:
  - id: justfile
    resource: justfile
    title: the gen-project and gen-doc recipes
  - id: project
    resource: project
    title: the folders
  - id: precommit
    resource: .pre-commit-config.yaml
    title: the exclude pattern
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:41:26Z"
status: draft
---

# Generated artefacts

`just gen-project` runs LinkML's generators over the schema with the settings in `.linkml/generators.yaml`, moves the Python dataclasses into `src/datatype/datamodel/`, and writes the Pydantic models beside them.[^justfile] `project/` holds the output: JSON Schema, OWL, SHACL, ShEx, the JSON-LD context and document, GraphQL, protobuf, SQL, TypeScript, an Excel workbook, a prefix map and a Java class for each of the eight classes.[^project]

`just gen-doc` writes `docs/schema/datatype.yaml`, the merged schema, and the element pages under `docs/elements/`, which git ignores. A schema change reruns both, and the pre-commit hooks leave their output alone.[^precommit]

[^justfile]: justfile, the gen-project and gen-doc recipes
[^project]: project, the folders
[^precommit]: .pre-commit-config.yaml, the exclude pattern
