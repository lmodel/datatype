---
type: Explanation
id: https://w3id.org/lmodel/datatype/knowledge/explanations/departures-from-owl
genre: explanation
title: How the schema departs from OWL
description: "Where the LinkML schema differs from the OWL ontology it renders: closed classes, IRIs in place of individuals, a pattern for the fixed PERCENT unit, three rules of this project's own (a percent between 0 and 100, a non-negative uncertainty, min not above max), and the one rule no validator checks."
resource: docs/about.md
sources:
  - id: about
    resource: docs/about.md
    title: How it departs from OWL
  - id: index
    resource: docs/index.md
    title: Validating data
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:41:26Z"
status: draft
---

# How the schema departs from OWL

OWL leaves a class open to any property, and LinkML closes it, so a value carries only the properties its class's restrictions name. A unit, a vocabulary and a concept are given by their IRIs, and the validator cannot check what an IRI names. The ontology fixes a percent's unit with `owl:hasValue`, and the schema states it as a pattern that admits that one IRI.[^about]

Three rules are this project's, not the ontology's: a percent lies between 0 and 100, an uncertainty is not negative, and a range's `min` is not above its `max`. The validator checks the first two. No validator can compare two slots, so `tests/test_data.py` checks the third over the examples.[^index] The generated dataclasses check no bound or pattern, and the Pydantic models read a word such as "yes" as a true `Boolean`, so data is validated before it is loaded.[^index]

[^about]: docs/about.md, How it departs from OWL
[^index]: docs/index.md, Validating data
