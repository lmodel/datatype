---
type: GlossaryTerm
id: https://w3id.org/lmodel/datatype/knowledge/glossary/datatype-concept
genre: reference
title: Concept (data:Concept)
description: "The Datatype Ontology's `data:Concept`: class to encapsulate a classifier, usually a values from a controlled vocabulary. A `Concept` holds exactly one concept by its IRI in `rdf_value`, RDF's `rdf:value`, and exactly one `vocabulary`, the IRI of the vocabulary it comes from. The adapt copy names the class `DatatypeConcept`, since LOKF defines `Concept`."
definition: Class to encapsulate a classifier, usually a values from a controlled vocabulary
resource: src/datatype/schema/datatype.yaml
definedBy:
  - https://w3id.org/lmodel/datatype/knowledge/references/datatype-ontology
relatedTo:
  - https://w3id.org/lmodel/datatype/knowledge/datasets/datatype-linkml-schema
sources:
  - id: ttl
    resource: upstream/rdf/datatype.ttl
    title: data:Concept
  - id: datatype.yaml
    resource: src/datatype/schema/datatype.yaml
    title: the class Concept
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:41:26Z"
status: draft
---

# Concept (data:Concept)

The ontology defines `data:Concept` as "Class to encapsulate a classifier, usually a values from a controlled vocabulary".[^ttl] A `Concept` holds exactly one concept by its IRI in `rdf_value`, RDF's `rdf:value`, and exactly one `vocabulary`, the IRI of the vocabulary it comes from. The adapt copy names the class `DatatypeConcept`, since LOKF defines `Concept`.[^datatype.yaml]

[^ttl]: upstream/rdf/datatype.ttl, data:Concept
[^datatype.yaml]: src/datatype/schema/datatype.yaml, the class Concept
