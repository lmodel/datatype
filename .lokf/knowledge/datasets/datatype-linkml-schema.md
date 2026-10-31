---
type: Dataset
id: https://w3id.org/lmodel/datatype/knowledge/datasets/datatype-linkml-schema
genre: reference
title: Datatype LinkML schema
description: "The LinkML schema `src/datatype/schema/datatype.yaml`: the Datatype Ontology's eight classes and seven properties, and `rdf_value` for RDF's `rdf:value`, each with the ontology's local name and IRI under `data:`, at the ontology's edition of 2019-10-03."
resource: src/datatype/schema/datatype.yaml
derivedFrom:
  - https://w3id.org/lmodel/datatype/knowledge/references/datatype-ontology
sources:
  - id: datatype.yaml
    resource: src/datatype/schema/datatype.yaml
    title: the header, the slots and the classes
  - id: linkmllint
    resource: .linkmllint.yaml
    title: the canonical_prefixes setting
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:41:26Z"
status: draft
---

# Datatype LinkML schema

`src/datatype/schema/datatype.yaml` is the schema, named `datatype`, with the id `https://w3id.org/lmodel/datatype`. Its header gives the version `2019-10-03`, the ontology's `dcterms:modified` date, the source `http://linked.data.gov.au/def/datatype` and the Apache-2.0 licence. Its annotations name the upstream commit, the ontology's creator and its two licences.[^datatype.yaml]

The schema binds the ontology's namespace under `data:` and its own under `datatype_linkml:`, `https://w3id.org/lmodel/datatype/`. Its classes are `Boolean`, `Concept`, `Count`, `Percent`, `PercentRange`, `QuantitativeMeasure`, `QuantitativeRange` and `Text`. Its slots are `value`, `min`, `max`, `uncertainty`, `standard`, `unit`, `vocabulary` and `rdf_value`. Each class carries the slots the ontology's restrictions name, with their cardinalities and datatypes. `Percent` and `PercentRange` fix the unit to QUDT's PERCENT with a pattern. The schema carries no mapping.[^datatype.yaml]

`.linkmllint.yaml` relaxes one lint rule: `canonical_prefixes` reads the Bioregistry and the linked-data context instead of the merged context, because prefix.cc gives `data:` to an unrelated site.[^linkmllint]

[^datatype.yaml]: src/datatype/schema/datatype.yaml, the header, the slots and the classes
[^linkmllint]: .linkmllint.yaml, the canonical_prefixes setting
