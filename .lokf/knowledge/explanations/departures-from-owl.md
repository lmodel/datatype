---
type: Explanation
id: https://w3id.org/lmodel/datatype/knowledge/explanations/departures-from-owl
genre: explanation
title: How the schema departs from OWL
description: "Where the LinkML schema differs from the OWL ontology it renders: closed classes, IRIs in place of individuals, a pattern for the fixed PERCENT unit, no bound on any value, and one rule of this project's own that no validator checks: a range's min is not above its max."
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
  at: "2026-10-31T12:51:35Z"
status: draft
---

# How the schema departs from OWL

OWL leaves a class open to any property, and LinkML closes it, so a value carries only the properties its class's restrictions name. A unit, a vocabulary and a concept are given by their IRIs, and the validator cannot check what an IRI names. The ontology fixes a percent's unit with `owl:hasValue`, and the schema states it as a pattern that admits that one IRI.[^about]

The validator checks no bound, since the ontology states none. One rule is this project's, and the ontology does not state it: a range's `min` is not above its `max`. No validator can compare two slots, so the validator accepts such a range and `tests/test_data.py` checks the rule over the examples.[^index] The generated dataclasses check no pattern, and the Pydantic models read a word such as "yes" as a true `Boolean`, so data is validated before it is loaded.[^index]

[^about]: docs/about.md, How it departs from OWL
[^index]: docs/index.md, Validating data
