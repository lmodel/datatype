---
type: GlossaryTerm
id: https://w3id.org/lmodel/datatype/knowledge/glossary/text
genre: reference
title: Text
description: "The Datatype Ontology's `data:Text`: class to encapsulate a textual value. A `Text` holds exactly one `value`, a string."
definition: Class to encapsulate a textual value
resource: src/datatype/schema/datatype.yaml
definedBy:
  - https://w3id.org/lmodel/datatype/knowledge/references/datatype-ontology
relatedTo:
  - https://w3id.org/lmodel/datatype/knowledge/datasets/datatype-linkml-schema
sources:
  - id: ttl
    resource: upstream/rdf/datatype.ttl
    title: data:Text
  - id: datatype.yaml
    resource: src/datatype/schema/datatype.yaml
    title: the class Text
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:41:26Z"
status: draft
---

# Text

The ontology defines `data:Text` as "Class to encapsulate a textual value".[^ttl] A `Text` holds exactly one `value`, a string.[^datatype.yaml]

[^ttl]: upstream/rdf/datatype.ttl, data:Text
[^datatype.yaml]: src/datatype/schema/datatype.yaml, the class Text
