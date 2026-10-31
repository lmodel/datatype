# datatype

This project is a LinkML rendering of the Datatype Ontology of the Australian
Government Linked Data Working Group (AGLDWG), by Simon Cox of CSIRO, at its
edition of 3 October 2019. Its eight classes each wrap one value: a text, a
true-or-false value, a count, a concept from a vocabulary, a measure with its
unit, a range, a percent and a percent range. Each class and property keeps
the ontology's local name and IRI.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): where the schema comes from and how it departs from OWL
- [`datatype.yaml`](schema/datatype.yaml): the schema

## Validating data

`linkml-validate -s src/datatype/schema/datatype.yaml -C QuantitativeMeasure measure.yaml`
checks a file against the JSON Schema generated from the schema, and
`tests/test_data.py` holds every example to it and to the committed
`project/jsonschema/datatype.schema.json`.

The validator checks the ontology's restrictions:

- the one value of a `Text`, `Boolean`, `Count` or `QuantitativeMeasure`,
  and its datatype;
- the one unit of a measure or range;
- the one `min` and `max` of a range;
- at most one `uncertainty`;
- the one concept and vocabulary of a `Concept`;
- QUDT's PERCENT as the only unit of a `Percent` or `PercentRange`.

It checks no rule the ontology does not state, so it accepts a percent above
100, a negative uncertainty and a range whose `min` is above its `max`.

Validate a file before loading it into either model in
`src/datatype/datamodel/`. LinkML 1.12.1 generates models that check less:

- The dataclasses check required fields, but no pattern. They turn a number
  or a list given as a `Text` into a string, and cut a `Count` of 2.5 to 2.
- The Pydantic models check patterns, but read a word such as `"yes"` as a
  true `Boolean`.
