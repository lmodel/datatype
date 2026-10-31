---
type: Explanation
id: https://w3id.org/lmodel/datatype/knowledge/explanations/scope-and-influences
genre: explanation
title: Scope, influences and mappings
description: What the schema models (the Datatype Ontology at its 2019-10-03 edition), what it leaves out (properties a class's restrictions do not name, what an IRI names, the ontology's other serialisations), its one-line influences, and why it carries no mapping.
resource: README.md
sources:
  - id: readme
    resource: README.md
    title: What it models, Influences, Mappings and Not modelled here
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:41:26Z"
status: draft
---

# Scope, influences and mappings

The schema renders one publication, the Datatype Ontology, at its edition of 2019-10-03, and its release asset and governance files follow lmodel/slsa.[^readme] It carries no mapping, because the ontology states no alignment to another vocabulary; its one link outward is that `value`, `min`, `max` and `uncertainty` are sub-properties of `rdf:value`.[^readme]

It leaves out:

- properties a class's restrictions do not name, which OWL allows and LinkML's closed classes do not;
- what an IRI names, such as a `Concept`'s value being a `skos:Concept`, which no validator can check;
- the ontology's RDF/XML, JSON-LD and HTML forms, which hold the same terms as the Turtle file.[^readme]

[^readme]: README.md, What it models, Influences, Mappings and Not modelled here
