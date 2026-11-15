---
type: Service
id: https://w3id.org/lmodel/datatype/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: "The Hugo site in `website/`, for <https://lmodel.github.io/datatype>: the README as its home page, the pages of `docs/`, a page per schema element, a page per concept of this bundle with its trust label, the bundle's exports, and redirects from the retired mkdocs site's pages, built and published by Knowledge website."
resource: website
sources:
  - id: site-config
    resource: website/site.toml
    title: the site's address, title and redirects
  - id: website-readme
    resource: website/README.md
    title: the build
generated:
  by: process:ktl-librarian
  at: "2026-11-15T03:03:20Z"
status: draft
---

# Documentation site

`website/` is a Hugo site from the ktl-website template, for `https://lmodel.github.io/datatype`.[^site-config] It shows the README as its home page, the pages of `docs/`, a page per class, slot, enumeration and type of `src/datatype/schema/datatype.yaml`, written by LinkML's `gen-doc` and each also at `elements/<Name>/`, and a page per concept of the bundle with its trust label.[^website-readme]

`scripts/build.sh`, run in `website/`, writes the site to `dist/` with its search index and then checks every link between its pages. Hugo and Pagefind come from PyPI through uv, so the build needs bash, git and uv. `scripts/build.sh serve` serves the site at `http://localhost:1313/datatype/` and rebuilds it as you edit.[^website-readme]

The redirects in `website/site.toml` keep the retired mkdocs site's addresses working:

- three types of the old schema's own go to the LinkML type that replaced them;
- four others go to the schema index;
- `/about` goes to the docs' about page.[^site-config]

The Knowledge website workflow publishes it.

[^site-config]: website/site.toml, the site's address, title and redirects
[^website-readme]: website/README.md, the build
