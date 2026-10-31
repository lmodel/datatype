---
type: Dataset
id: https://w3id.org/lmodel/datatype/knowledge/datasets/lokf-adapt-copy
genre: reference
title: The adapt copy (.lokf/datatype.yaml)
description: "`.lokf/datatype.yaml`, the copy `lokf adapt` writes from the schema for knowledge bundles: rooted on no class, with `Concept` renamed `DatatypeConcept` and `unit` renamed `datatype_unit`, keeping their IRIs. A release attaches it as `schema-<tag>-datatype.yaml`."
resource: .lokf/datatype.yaml
derivedFrom:
  - https://w3id.org/lmodel/datatype/knowledge/datasets/datatype-linkml-schema
sources:
  - id: project.justfile
    resource: project.justfile
    title: the knowledge bundle recipes and their comment
  - id: lokf-justfile
    resource: .lokf/justfile
    title: the schema line
  - id: copy
    resource: .lokf/datatype.yaml
    title: DatatypeConcept and datatype_unit
  - id: rules
    resource: tests/test_schema_rules.py
    title: SHARED_WITH_NEIGHBOURS and the renames
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:41:26Z"
status: draft
---

# The adapt copy (.lokf/datatype.yaml)

`just lokf-adapt` writes `.lokf/datatype.yaml` from the schema with `--prefix datatype`, and `just lokf-adapt-check` fails when the copy is stale. The recipes root the copy on no class: every class is a value a concept holds, and no class carries an identifier.[^project.justfile] The sidecar's justfile names the copy on its `schema :=` line, so the bundle validates against it.[^lokf-justfile]

LOKF defines `Concept` and `unit`, so the copy renames them `DatatypeConcept` and `datatype_unit`, with the ontology's IRIs `data:Concept` and `data:unit` and their old names as aliases.[^copy] The copy shares one key, `value`, with the released copies of attack, in-toto, oscal, slsa, spdx and stix, each under its own IRI. `tests/test_schema_rules.py` lists that key and fails on a new shared name.[^rules]

[^project.justfile]: project.justfile, the knowledge bundle recipes and their comment
[^lokf-justfile]: .lokf/justfile, the schema line
[^copy]: .lokf/datatype.yaml, DatatypeConcept and datatype_unit
[^rules]: tests/test_schema_rules.py, SHARED_WITH_NEIGHBOURS and the renames
