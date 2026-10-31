---
type: Service
id: https://w3id.org/lmodel/datatype/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: "The Astro Starlight site in `website/`, for <https://lmodel.github.io/datatype>: the README as its home page, the pages of `docs/`, a page per schema element, a page per concept of this bundle with its trust label, the bundle's exports, and redirects from the retired mkdocs site's pages, built and published by Knowledge website."
resource: website
sources:
  - id: site-config
    resource: website/site.config.mjs
    title: REPO, SITE, BASE, DOCS and REDIRECTS
  - id: website-readme
    resource: website/README.md
    title: the build
generated:
  by: process:ktl-librarian
  at: "2026-10-31T12:41:26Z"
status: draft
---

# Documentation site

`website/` is an Astro Starlight site from the ktl-website template, for `https://lmodel.github.io/datatype`. `npm run build` syncs the README, the pages of `docs/`, the schema's element pages and the bundle into it, builds it and checks every link.[^website-readme]

Its `REDIRECTS` keep the retired mkdocs site's addresses working. `/elements/` and each element page go to the schema pages, three types of the old schema's own go to the LinkML type that replaced them, four others go to the schema index, and `/about` goes to the docs' about page.[^site-config] The Knowledge website workflow publishes it.

[^site-config]: website/site.config.mjs, REPO, SITE, BASE, DOCS and REDIRECTS
[^website-readme]: website/README.md, the build
