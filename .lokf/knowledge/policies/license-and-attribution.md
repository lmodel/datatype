---
type: Policy
id: https://w3id.org/lmodel/datatype/knowledge/policies/license-and-attribution
genre: reference
title: Licence and attribution
description: "The licences: Apache-2.0 for the schema and the code, CC BY 4.0 for the knowledge bundle, and for the Datatype Ontology CC0 1.0 in its own metadata and CC BY 4.0 in its repository, of which NOTICE follows the stricter with an attribution to Simon Cox, CSIRO and the AGLDWG."
resource: NOTICE
sources:
  - id: readme
    resource: README.md
    title: License
  - id: notice
    resource: NOTICE
    title: every section
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:41:26Z"
status: draft
---

# Licence and attribution

The schema and the code are under the Apache License 2.0, and the knowledge bundle under CC BY 4.0, as its `index.md` declares.[^readme]

The ontology's own `dcterms:license` is CC0 1.0, and its repository's `LICENSE`, added later, is CC BY 4.0. `NOTICE` follows the stricter of the two: it attributes the ontology to Simon J.D. Cox of CSIRO and the AGLDWG, names the licence, links to the material and says what was changed. Each description in the schema is the ontology's `skos:definition`.[^notice] It also names the MIT licence of the linkml-project-copier template and the Apache-2.0 licence of the KTL templates.[^notice]

[^readme]: README.md, License
[^notice]: NOTICE, every section
