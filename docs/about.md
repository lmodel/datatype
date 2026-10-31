# About datatype

The schema renders the [Datatype Ontology](http://linked.data.gov.au/def/datatype),
whose source is [AGLDWG/datatype-ont](https://github.com/AGLDWG/datatype-ont).
`upstream/` copies the ontology's Turtle file and the repository's licence at
commit `dd8f24120cd5`, the head of `master` since 4 June 2021, and the
schema's tests read that copy.

## Names and IRIs

Each class and property keeps its local name and its IRI under `data:`,
`http://linked.data.gov.au/def/datatype/`. Its title is the ontology's
`rdfs:label`, and its description the ontology's `skos:definition`. One slot
comes from outside the ontology: `rdf_value`, RDF's `rdf:value`, which the
ontology uses for a `Concept` and names as the parent of `value`, `min`, `max`
and `uncertainty`. What the schema adds sits under `datatype_linkml:`,
`https://w3id.org/lmodel/datatype/`.

## How it departs from OWL

- **Closed classes.** OWL leaves a class open to any property, and LinkML
  closes it, so a value carries only the properties its class's restrictions
  name.
- **IRIs, not individuals.** A unit, a vocabulary and a concept are given by
  their IRIs. The validator cannot check that a vocabulary's IRI names a SKOS
  scheme or an OWL ontology, as the ontology's range says.
- **A pattern for a fixed value.** The ontology fixes a percent's unit with
  `owl:hasValue`. The schema states it as a pattern that admits that one IRI,
  `http://qudt.org/vocab/unit/PERCENT`.
- **Three rules of this project's own**, which [the home page](index.md)
  lists.

## Licence

The ontology states CC0 1.0, and its repository's licence is CC BY 4.0. The
repository's [NOTICE](https://github.com/lmodel/datatype/blob/main/NOTICE)
gives the attribution that CC BY 4.0 asks for.
