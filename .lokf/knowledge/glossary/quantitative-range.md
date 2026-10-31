---
type: GlossaryTerm
id: https://w3id.org/lmodel/datatype/knowledge/glossary/quantitative-range
genre: reference
title: Quantitative Range
description: "The Datatype Ontology's `data:QuantitativeRange`: class to encapsulate a quantitative range. A `QuantitativeRange` holds exactly one `min` and one `max`, decimals, exactly one `unit` and at most one `uncertainty`."
definition: Class to encapsulate a quantitative range
resource: src/datatype/schema/datatype.yaml
definedBy:
  - https://w3id.org/lmodel/datatype/knowledge/references/datatype-ontology
relatedTo:
  - https://w3id.org/lmodel/datatype/knowledge/datasets/datatype-linkml-schema
sources:
  - id: ttl
    resource: upstream/rdf/datatype.ttl
    title: data:QuantitativeRange
  - id: datatype.yaml
    resource: src/datatype/schema/datatype.yaml
    title: the class QuantitativeRange
generated:
  by: process:ktl-librarian
  at: "2026-10-31T18:02:18Z"
status: draft
---

# Quantitative Range

The ontology defines `data:QuantitativeRange` as "Class to encapsulate a quantitative range".[^ttl] A `QuantitativeRange` holds exactly one `min` and one `max`, decimals, exactly one `unit` and at most one `uncertainty`.[^datatype.yaml]

[^ttl]: upstream/rdf/datatype.ttl, data:QuantitativeRange
[^datatype.yaml]: src/datatype/schema/datatype.yaml, the class QuantitativeRange
