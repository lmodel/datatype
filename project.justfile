## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# ============ Knowledge bundle: the adapted domain schema ============

# `.lokf/datatype.yaml` is the copy `lokf adapt` writes from the schema so
# that it can sit beside `.lokf/lokf.yaml` (`lokf adapt --help` lists the
# moves). The roots would be the classes a knowledge concept may use as its
# `type`, and there are none: every class of the Datatype Ontology is a value
# that a concept holds, such as a measure or a range, never a thing a concept
# is. No class carries an identifier, which is what lokf 0.9.0's adapt roots
# by default, so the copy is rooted on nothing and a host imports its classes
# as the ranges of its own concept classes' slots. A name the copy shares
# with lokf.yaml takes the prefix `datatype`, keeping its IRI: Concept
# becomes DatatypeConcept, and unit becomes datatype_unit. The recipes run
# the `lokf` the sidecar's floor pins (0.9.0 or later); LOKF_CMD runs
# another, such as a checkout:
# LOKF_CMD="uv run --project ../lokf lokf" just lokf-adapt
lokf_cmd := env_var_or_default("LOKF_CMD", "uv run --project .lokf lokf")
lokf_adapt_roots := ""

# Rewrite .lokf/datatype.yaml from the schema (run after every schema change)
[group('knowledge bundle')]
lokf-adapt:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --prefix datatype --lokf .lokf/lokf.yaml -o .lokf/datatype.yaml

# Fail when .lokf/datatype.yaml is stale against the schema or .lokf/lokf.yaml
[group('knowledge bundle')]
lokf-adapt-check:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --prefix datatype --lokf .lokf/lokf.yaml -o .lokf/datatype.yaml --check
