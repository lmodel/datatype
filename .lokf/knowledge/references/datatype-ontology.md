---
type: Reference
id: https://w3id.org/lmodel/datatype/knowledge/references/datatype-ontology
genre: reference
title: The Datatype Ontology
description: The Datatype Ontology ("Datatypes"), <http://linked.data.gov.au/def/datatype>, by Simon J.D. Cox of CSIRO, published by the Australian Government Linked Data Working Group (AGLDWG) at AGLDWG/datatype-ont. It was last changed on 2019-10-03, states no version number, and is licensed CC0 1.0 in its own metadata and CC BY 4.0 in its repository.
resource: http://linked.data.gov.au/def/datatype
sources:
  - id: ttl
    resource: upstream/rdf/datatype.ttl
    title: the ontology's header
  - id: notice
    resource: NOTICE
    title: The Datatype Ontology
  - id: watch
    resource: scripts/check_upstream_release.py
    title: PINNED_REDIRECT and the module docstring
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:41:26Z"
status: draft
---

# The Datatype Ontology

The ontology's Turtle file gives its label, "Datatypes", its creator, Simon J.D. Cox of CSIRO, its creation on 2019-03-25 and its last change on 2019-10-03. It describes itself as a set of classes representing data-types, for observation results or the range of properties where scaled numbers, ranges or percents are required. Its history note says it was first written for the TERN-plot ontology. It states `dcterms:license` CC0 1.0, and no `owl:versionInfo` or `owl:versionIRI`.[^ttl]

The AGLDWG publishes it from the `master` branch of AGLDWG/datatype-ont, whose last commit, on 4 June 2021, added a CC BY 4.0 `LICENSE`. The repository has no tag or release.[^notice] Its namespace redirects a request for Turtle to that branch's `rdf/datatype.ttl` through raw.githack.com.[^watch]

[^ttl]: upstream/rdf/datatype.ttl, the ontology's header
[^notice]: NOTICE, The Datatype Ontology
[^watch]: scripts/check_upstream_release.py, PINNED_REDIRECT and the module docstring
