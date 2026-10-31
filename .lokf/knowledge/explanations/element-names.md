---
type: Explanation
id: https://w3id.org/lmodel/datatype/knowledge/explanations/element-names
genre: explanation
title: Element names and IRIs
description: Why each class and slot keeps the Datatype Ontology's local name and IRI under `data:`, why `rdf_value` renders RDF's `rdf:value`, what the adapt copy renames, and the key `value` it shares with six neighbours.
resource: docs/about.md
sources:
  - id: about
    resource: docs/about.md
    title: Names and IRIs
  - id: datatype.yaml
    resource: src/datatype/schema/datatype.yaml
    title: the slot rdf_value
  - id: readme
    resource: README.md
    title: Knowledge Trust Ladder (KTL)
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:41:26Z"
status: draft
---

# Element names and IRIs

Each class and property keeps the ontology's local name and its IRI under `data:`, its title is the ontology's `rdfs:label`, and its description the ontology's `skos:definition`. What the schema adds sits under `datatype_linkml:`.[^about] The one slot from outside the ontology is `rdf_value`, RDF's `rdf:value`, which the ontology uses for a `Concept` and names as the parent of `value`, `min`, `max` and `uncertainty`; the schema states that parent with `is_a`.[^datatype.yaml]

LOKF defines `Concept` and `unit`, so the adapt copy renames them `DatatypeConcept` and `datatype_unit`, keeping their IRIs. The copy's key `value` is also a key of six released lmodel copies, each under its own IRI, so a host imports this copy beside none of them until `lokf adapt` can rename what a neighbour defines.[^readme]

[^about]: docs/about.md, Names and IRIs
[^datatype.yaml]: src/datatype/schema/datatype.yaml, the slot rdf_value
[^readme]: README.md, Knowledge Trust Ladder (KTL)
