---
type: GlossaryTerm
id: https://w3id.org/lmodel/datatype/knowledge/glossary/quantitative-measure
genre: reference
title: Quantitative Measure
description: "The Datatype Ontology's `data:QuantitativeMeasure`: class to encapsulate a quantitative measure value. A `QuantitativeMeasure` holds exactly one `value`, a decimal, exactly one `unit`, given by its IRI, and at most one `uncertainty`."
definition: Class to encapsulate a quantitative measure value
resource: src/datatype/schema/datatype.yaml
definedBy:
  - https://w3id.org/lmodel/datatype/knowledge/references/datatype-ontology
relatedTo:
  - https://w3id.org/lmodel/datatype/knowledge/datasets/datatype-linkml-schema
sources:
  - id: ttl
    resource: upstream/rdf/datatype.ttl
    title: data:QuantitativeMeasure
  - id: datatype.yaml
    resource: src/datatype/schema/datatype.yaml
    title: the class QuantitativeMeasure
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:41:26Z"
status: draft
---

# Quantitative Measure

The ontology defines `data:QuantitativeMeasure` as "Class to encapsulate a quantitative measure value".[^ttl] A `QuantitativeMeasure` holds exactly one `value`, a decimal, exactly one `unit`, given by its IRI, and at most one `uncertainty`.[^datatype.yaml]

[^ttl]: upstream/rdf/datatype.ttl, data:QuantitativeMeasure
[^datatype.yaml]: src/datatype/schema/datatype.yaml, the class QuantitativeMeasure
