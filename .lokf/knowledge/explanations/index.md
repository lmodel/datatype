# Explanations

* [Scope, influences and mappings](scope-and-influences.md) - What the schema models (the Datatype Ontology at its 2019-10-03 edition), what it leaves out (properties a class's restrictions do not name, what an IRI names, the ontology's other serialisations), its one-line influences, and why it carries no mapping.
* [Element names and IRIs](element-names.md) - Why each class and slot keeps the Datatype Ontology's local name and IRI under `data:`, why `rdf_value` renders RDF's `rdf:value`, what the adapt copy renames, and the key `value` it shares with six neighbours.
* [How the schema departs from OWL](departures-from-owl.md) - Where the LinkML schema differs from the OWL ontology it renders: closed classes, IRIs in place of individuals, a pattern for the fixed PERCENT unit, no bound on any value, and one rule of this project's own that no validator checks: a range's min is not above its max.
