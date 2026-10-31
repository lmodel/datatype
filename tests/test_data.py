"""Checks the example data against the schema.

Each valid example under tests/data/valid/ must load into the generated
dataclasses, pass the validator and keep the rule no validator checks. Each
counter-example under tests/data/invalid/ must fail the validator at the
place its first line names, as `# Fails at: <JSON pointer>`, and nowhere
else. A counter-example to the rule no validator checks sits under
tests/data/problem/invalid/, the template's folder for invalid data the
schema does not reject, since the template's example runner fails any
counter-example the validator accepts; it must break the rule at the place
its first line names, and pass the validator. The class an example is
checked against is the part of its file name before the first `-`.
"""

import functools
import json
from pathlib import Path

import jsonschema
import pytest
import yaml
from linkml.validator import validate
from linkml_runtime.loaders import yaml_loader

import datatype.datamodel.datatype

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "datatype" / "schema" / "datatype.yaml"
GENERATED_JSON_SCHEMA = ROOT / "project" / "jsonschema" / "datatype.schema.json"
DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"
DATA_DIR_RULES = Path(__file__).parent / "data" / "problem" / "invalid"
VALID_EXAMPLE_FILES = sorted(DATA_DIR_VALID.glob("*.yaml"))
INVALID_EXAMPLE_FILES = sorted(DATA_DIR_INVALID.glob("*.yaml"))
RULE_EXAMPLE_FILES = sorted(DATA_DIR_RULES.glob("*.yaml"))


def _target(path: Path) -> str:
    return path.stem.split("-")[0]


def _pointer(text: str, name: str) -> str:
    first = text.splitlines()[0]
    assert first.startswith("# Fails at: "), (
        f"{name}: the first line names where it fails"
    )
    return first.removeprefix("# Fails at: ").strip()


# The rule the schema's comments name as beyond the validator: no validator
# can compare two slots of one object. Each problem is a message in the
# validator's own form, ending in the place it is at.
RANGES = ("QuantitativeRange", "PercentRange")


def rule_problems(target: str, data: dict) -> list[str]:
    """Each break of the rule no validator checks: a range's min is not
    above its max."""
    problems = []
    if target in RANGES and isinstance(data, dict):
        low, high = data.get("min"), data.get("max")
        if (
            isinstance(low, (int, float))
            and isinstance(high, (int, float))
            and low > high
        ):
            problems.append(f"min {low} is above max {high} in /min")
    return problems


def _validator_messages(data, target: str) -> list[str]:
    return [r.message for r in validate(data, str(SCHEMA), target).results]


def _messages(text: str, target: str) -> list[str]:
    """Every message the validator gives, and every rule problem."""
    data = yaml.safe_load(text)
    return _validator_messages(data, target) + rule_problems(target, data)


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES, ids=lambda p: p.name)
def test_valid_data_files(filepath):
    """Each valid example loads into the generated dataclasses."""
    target = getattr(datatype.datamodel.datatype, _target(filepath))
    assert yaml_loader.load(str(filepath), target_class=target)


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES, ids=lambda p: p.name)
def test_valid_data_files_validate(filepath):
    """Each valid example passes the validator and keeps the rule."""
    messages = _messages(filepath.read_text(), _target(filepath))
    assert not messages, messages


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES, ids=lambda p: p.name)
def test_invalid_data_files_fail(filepath):
    """Each counter-example fails the validator at the place its first line
    names, and at no other, so a file that starts failing for another
    reason fails this test."""
    text = filepath.read_text()
    pointer = _pointer(text, filepath.name)
    messages = _messages(text, _target(filepath))
    assert messages, f"{filepath.name} passes"
    assert all(m.endswith(f" in {pointer}") for m in messages), messages


@pytest.mark.parametrize("filepath", RULE_EXAMPLE_FILES, ids=lambda p: p.name)
def test_rule_counter_examples_break_the_rule_only(filepath):
    """Each counter-example to the rule passes the validator and breaks the
    rule at the place its first line names, and at no other."""
    text = filepath.read_text()
    pointer = _pointer(text, filepath.name)
    data = yaml.safe_load(text)
    assert not _validator_messages(data, _target(filepath))
    problems = rule_problems(_target(filepath), data)
    assert problems, f"{filepath.name} keeps the rule"
    assert all(m.endswith(f" in {pointer}") for m in problems), problems


def test_every_class_has_an_example():
    """Each class has a valid example, each counter-example names a class
    of the schema, and the rule has a counter-example."""
    classes = set(yaml.safe_load(SCHEMA.read_text())["classes"])
    examples = {_target(f) for f in VALID_EXAMPLE_FILES}
    assert classes <= examples, sorted(classes - examples)
    assert {_target(f) for f in INVALID_EXAMPLE_FILES + RULE_EXAMPLE_FILES} <= classes
    assert {_target(f) for f in RULE_EXAMPLE_FILES} == {"QuantitativeRange"}


# The committed project/jsonschema file is what a host that validates with
# JSON Schema alone reads, so the examples hold it to the same results.


@functools.cache
def _generated() -> dict:
    return json.loads(GENERATED_JSON_SCHEMA.read_text())


def _generated_failures(data, target: str) -> list[str]:
    schema = {**_generated(), "$ref": f"#/$defs/{target}"}
    cls = jsonschema.validators.validator_for(schema)
    return [
        "/" + "/".join(str(p) for p in e.absolute_path)
        for e in cls(schema, format_checker=cls.FORMAT_CHECKER).iter_errors(data)
    ]


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES, ids=lambda p: p.name)
def test_valid_data_files_pass_the_generated_json_schema(filepath):
    """Each valid example passes the committed JSON Schema."""
    failures = _generated_failures(
        yaml.safe_load(filepath.read_text()), _target(filepath)
    )
    assert not failures, failures


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES, ids=lambda p: p.name)
def test_invalid_data_files_fail_the_generated_json_schema(filepath):
    """Each counter-example fails the committed JSON Schema at the same
    place as the validator."""
    text = filepath.read_text()
    pointer = _pointer(text, filepath.name)
    failures = _generated_failures(yaml.safe_load(text), _target(filepath))
    assert failures and all(f == pointer for f in failures), failures
