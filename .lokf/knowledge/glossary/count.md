---
type: GlossaryTerm
id: https://w3id.org/lmodel/datatype/knowledge/glossary/count
genre: reference
title: Count
description: "The Datatype Ontology's `data:Count`: class to encapsulate an integer value. A `Count` holds exactly one `value`, an integer, and at most one `uncertainty`."
definition: Class to encapsulate an integer value
resource: src/datatype/schema/datatype.yaml
definedBy:
  - https://w3id.org/lmodel/datatype/knowledge/references/datatype-ontology
relatedTo:
  - https://w3id.org/lmodel/datatype/knowledge/datasets/datatype-linkml-schema
sources:
  - id: ttl
    resource: upstream/rdf/datatype.ttl
    title: data:Count
  - id: datatype.yaml
    resource: src/datatype/schema/datatype.yaml
    title: the class Count
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:41:26Z"
status: draft
---

# Count

The ontology defines `data:Count` as "Class to encapsulate an integer value".[^ttl] A `Count` holds exactly one `value`, an integer, and at most one `uncertainty`.[^datatype.yaml]

[^ttl]: upstream/rdf/datatype.ttl, data:Count
[^datatype.yaml]: src/datatype/schema/datatype.yaml, the class Count
