---
type: GlossaryTerm
id: https://w3id.org/lmodel/datatype/knowledge/glossary/value-class
genre: reference
title: Value class
description: In this repository, a class whose instances are values a knowledge concept holds, such as a measure or a range, and never concepts themselves. Every class of the Datatype Ontology is one, so a host imports them as the ranges of its own concept classes' slots.
definition: A class whose instances are values a knowledge concept holds, never concepts themselves.
resource: project.justfile
relatedTo:
  - https://w3id.org/lmodel/datatype/knowledge/datasets/lokf-adapt-copy
sources:
  - id: project.justfile
    resource: project.justfile
    title: the comment on the knowledge bundle recipes
  - id: readme
    resource: README.md
    title: Knowledge Trust Ladder (KTL)
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:41:26Z"
status: draft
---

# Value class

The adapt recipes root the copy on no class, because every class of the Datatype Ontology is a value a concept holds, never a thing a concept is.[^project.justfile] A host's own concept class takes one as the range of a slot, such as a `height` that is a `QuantitativeMeasure`, and no concept names one as its `type`.[^readme]

[^project.justfile]: project.justfile, the comment on the knowledge bundle recipes
[^readme]: README.md, Knowledge Trust Ladder (KTL)
