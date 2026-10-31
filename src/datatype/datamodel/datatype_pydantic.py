from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.12.0"
version = "2019-10-03"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'annotations': {'upstream_branch': {'tag': 'upstream_branch',
                                         'value': 'master'},
                     'upstream_commit': {'tag': 'upstream_commit',
                                         'value': 'dd8f24120cd59f686086f58175de37807c569e18'},
                     'upstream_created': {'tag': 'upstream_created',
                                          'value': '2019-03-25'},
                     'upstream_creator': {'tag': 'upstream_creator',
                                          'value': 'Simon J.D. Cox, CSIRO, '
                                                   'https://orcid.org/0000-0002-3884-3420'},
                     'upstream_licence': {'tag': 'upstream_licence',
                                          'value': "CC0-1.0 in the ontology's "
                                                   'dcterms:license; CC-BY-4.0 in '
                                                   "the repository's LICENSE"},
                     'upstream_repository': {'tag': 'upstream_repository',
                                             'value': 'https://github.com/AGLDWG/datatype-ont'}},
     'comments': ['The ontology states no owl:versionInfo or owl:versionIRI, and '
                  'its repository has no tag or release, so the version is the '
                  "ontology's dcterms:modified date. upstream/ copies its Turtle "
                  'file and licence at the commit in the annotations, and '
                  'scripts/check_upstream_release.py reports when the master '
                  'branch moves.',
                  "The ontology's own dcterms:license is CC0 1.0, and the "
                  "repository's LICENSE, added later, is CC BY 4.0. Each "
                  "description is the ontology's skos:definition of the term, used "
                  'with the attribution NOTICE gives.',
                  'The classes are closed: a value carries only the properties the '
                  "ontology's restrictions on its class name. OWL leaves a class "
                  'open to other properties, so data that adds, say, a standard to '
                  'a QuantitativeMeasure is valid OWL but not valid here.'],
     'default_prefix': 'datatype_linkml',
     'default_range': 'string',
     'description': 'A LinkML rendering of the Datatype Ontology ("Datatypes") of '
                    'the Australian Government Linked Data Working Group (AGLDWG), '
                    'by Simon Cox of CSIRO. In its own words: a set of classes '
                    'representing data-types. These may be used for observation '
                    'results, or for the range of specific properties in other '
                    'applications where scaled numbers, ranges, percents etc are '
                    "required. Each class and property keeps the ontology's local "
                    'name and IRI.',
     'id': 'https://w3id.org/lmodel/datatype',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'datatype',
     'prefixes': {'data': {'prefix_prefix': 'data',
                           'prefix_reference': 'http://linked.data.gov.au/def/datatype/'},
                  'datatype_linkml': {'prefix_prefix': 'datatype_linkml',
                                      'prefix_reference': 'https://w3id.org/lmodel/datatype/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://lmodel.github.io/datatype',
                  'https://github.com/AGLDWG/datatype-ont/tree/dd8f24120cd59f686086f58175de37807c569e18'],
     'source': 'http://linked.data.gov.au/def/datatype',
     'source_file': 'src/datatype/schema/datatype.yaml',
     'title': 'Datatype Ontology'} )


class Boolean(ConfiguredBaseModel):
    """
    Class to encapsulate a true-or-false value
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'data:Boolean',
         'from_schema': 'https://w3id.org/lmodel/datatype',
         'slot_usage': {'value': {'name': 'value',
                                  'range': 'boolean',
                                  'required': True}},
         'title': 'Boolean'})

    value: bool = Field(default=..., title="data value", description="""simple value (a literal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Boolean', 'Count', 'QuantitativeMeasure', 'Text'],
         'is_a': 'rdf_value',
         'slot_uri': 'data:value'} })


class Concept(ConfiguredBaseModel):
    """
    Class to encapsulate a classifier, usually a values from a controlled vocabulary
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'data:Concept',
         'from_schema': 'https://w3id.org/lmodel/datatype',
         'slot_usage': {'rdf_value': {'comments': ['The concept by its IRI. The '
                                                   "ontology's range is a "
                                                   'skos:Concept, which the validator '
                                                   'cannot check of an IRI.'],
                                      'name': 'rdf_value',
                                      'range': 'uriorcurie',
                                      'required': True},
                        'vocabulary': {'name': 'vocabulary', 'required': True}},
         'title': 'Concept'})

    rdf_value: str = Field(default=..., title="value", description="""The main value of a structured value, as RDF's own rdf:value property names it. The ontology restricts it on Concept and makes value, min, max and uncertainty its sub-properties.""", json_schema_extra = { "linkml_meta": {'comments': ["The concept by its IRI. The ontology's range is a skos:Concept, "
                      'which the validator cannot check of an IRI.'],
         'domain_of': ['Concept'],
         'slot_uri': 'rdf:value'} })
    vocabulary: str = Field(default=..., title="vocabulary", description="""controlled vocabulary, taxonomy etc""", json_schema_extra = { "linkml_meta": {'comments': ["The vocabulary by its IRI. The ontology's range is a "
                      'skos:ConceptScheme, a skos:Collection or an owl:Ontology, which '
                      'the validator cannot check of an IRI.'],
         'domain_of': ['Concept'],
         'is_a': 'standard',
         'slot_uri': 'data:vocabulary'} })


class Count(ConfiguredBaseModel):
    """
    Class to encapsulate an integer value
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'data:Count',
         'from_schema': 'https://w3id.org/lmodel/datatype',
         'slot_usage': {'value': {'name': 'value',
                                  'range': 'integer',
                                  'required': True}},
         'title': 'Count'})

    value: int = Field(default=..., title="data value", description="""simple value (a literal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Boolean', 'Count', 'QuantitativeMeasure', 'Text'],
         'is_a': 'rdf_value',
         'slot_uri': 'data:value'} })
    uncertainty: Optional[Decimal] = Field(default=None, title="data uncertainty", description="""Uncertainty for a quantitative value""", json_schema_extra = { "linkml_meta": {'domain_of': ['Count', 'QuantitativeMeasure', 'QuantitativeRange'],
         'is_a': 'rdf_value',
         'slot_uri': 'data:uncertainty'} })


class QuantitativeMeasure(ConfiguredBaseModel):
    """
    Class to encapsulate a quantitative measure value
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'data:QuantitativeMeasure',
         'from_schema': 'https://w3id.org/lmodel/datatype',
         'slot_usage': {'unit': {'name': 'unit', 'required': True},
                        'value': {'name': 'value',
                                  'range': 'decimal',
                                  'required': True}},
         'title': 'Quantitative Measure'})

    value: Decimal = Field(default=..., title="data value", description="""simple value (a literal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Boolean', 'Count', 'QuantitativeMeasure', 'Text'],
         'is_a': 'rdf_value',
         'slot_uri': 'data:value'} })
    unit: str = Field(default=..., title="unit of measure", description="""Measurement scale""", json_schema_extra = { "linkml_meta": {'comments': ['The unit by its IRI, such as http://qudt.org/vocab/unit/M from '
                      'the QUDT units vocabulary. The ontology states no range.'],
         'domain_of': ['QuantitativeMeasure', 'QuantitativeRange'],
         'is_a': 'standard',
         'slot_uri': 'data:unit'} })
    uncertainty: Optional[Decimal] = Field(default=None, title="data uncertainty", description="""Uncertainty for a quantitative value""", json_schema_extra = { "linkml_meta": {'domain_of': ['Count', 'QuantitativeMeasure', 'QuantitativeRange'],
         'is_a': 'rdf_value',
         'slot_uri': 'data:uncertainty'} })


class QuantitativeRange(ConfiguredBaseModel):
    """
    Class to encapsulate a quantitative range
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'data:QuantitativeRange',
         'from_schema': 'https://w3id.org/lmodel/datatype',
         'slot_usage': {'max': {'name': 'max', 'required': True},
                        'min': {'name': 'min', 'required': True},
                        'unit': {'name': 'unit', 'required': True}},
         'title': 'Quantitative Range'})

    min: Decimal = Field(default=..., title="data minimum", description="""Minimum value of range""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantitativeRange'],
         'is_a': 'rdf_value',
         'slot_uri': 'data:min'} })
    max: Decimal = Field(default=..., title="data maximum", description="""Maximum value of a range""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantitativeRange'],
         'is_a': 'rdf_value',
         'slot_uri': 'data:max'} })
    unit: str = Field(default=..., title="unit of measure", description="""Measurement scale""", json_schema_extra = { "linkml_meta": {'comments': ['The unit by its IRI, such as http://qudt.org/vocab/unit/M from '
                      'the QUDT units vocabulary. The ontology states no range.'],
         'domain_of': ['QuantitativeMeasure', 'QuantitativeRange'],
         'is_a': 'standard',
         'slot_uri': 'data:unit'} })
    uncertainty: Optional[Decimal] = Field(default=None, title="data uncertainty", description="""Uncertainty for a quantitative value""", json_schema_extra = { "linkml_meta": {'domain_of': ['Count', 'QuantitativeMeasure', 'QuantitativeRange'],
         'is_a': 'rdf_value',
         'slot_uri': 'data:uncertainty'} })


class Percent(QuantitativeMeasure):
    """
    Class to encapsulate a quantitative measure expressed as a percent value
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'data:Percent',
         'from_schema': 'https://w3id.org/lmodel/datatype',
         'slot_usage': {'unit': {'comments': ["The ontology's owl:hasValue: the unit "
                                              "is QUDT's PERCENT and no other. A "
                                              'pattern states it, since equals_string '
                                              'needs a string range.'],
                                 'name': 'unit',
                                 'pattern': '^http://qudt\\.org/vocab/unit/PERCENT$'}},
         'title': 'Percent'})

    value: Decimal = Field(default=..., title="data value", description="""simple value (a literal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Boolean', 'Count', 'QuantitativeMeasure', 'Text'],
         'is_a': 'rdf_value',
         'slot_uri': 'data:value'} })
    unit: str = Field(default=..., title="unit of measure", description="""Measurement scale""", json_schema_extra = { "linkml_meta": {'comments': ["The ontology's owl:hasValue: the unit is QUDT's PERCENT and no "
                      'other. A pattern states it, since equals_string needs a string '
                      'range.'],
         'domain_of': ['QuantitativeMeasure', 'QuantitativeRange'],
         'is_a': 'standard',
         'slot_uri': 'data:unit'} })
    uncertainty: Optional[Decimal] = Field(default=None, title="data uncertainty", description="""Uncertainty for a quantitative value""", json_schema_extra = { "linkml_meta": {'domain_of': ['Count', 'QuantitativeMeasure', 'QuantitativeRange'],
         'is_a': 'rdf_value',
         'slot_uri': 'data:uncertainty'} })

    @field_validator('unit')
    def pattern_unit(cls, v):
        pattern=re.compile(r"^http://qudt\.org/vocab/unit/PERCENT$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid unit format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid unit format: {v}"
            raise ValueError(err_msg)
        return v


class PercentRange(QuantitativeRange):
    """
    Class to encapsulate a quantitative range expressed as in percent values
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'data:PercentRange',
         'from_schema': 'https://w3id.org/lmodel/datatype',
         'slot_usage': {'unit': {'comments': ["The ontology's owl:hasValue: the unit "
                                              "is QUDT's PERCENT and no other. A "
                                              'pattern states it, since equals_string '
                                              'needs a string range.'],
                                 'name': 'unit',
                                 'pattern': '^http://qudt\\.org/vocab/unit/PERCENT$'}},
         'title': 'Percent range'})

    min: Decimal = Field(default=..., title="data minimum", description="""Minimum value of range""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantitativeRange'],
         'is_a': 'rdf_value',
         'slot_uri': 'data:min'} })
    max: Decimal = Field(default=..., title="data maximum", description="""Maximum value of a range""", json_schema_extra = { "linkml_meta": {'domain_of': ['QuantitativeRange'],
         'is_a': 'rdf_value',
         'slot_uri': 'data:max'} })
    unit: str = Field(default=..., title="unit of measure", description="""Measurement scale""", json_schema_extra = { "linkml_meta": {'comments': ["The ontology's owl:hasValue: the unit is QUDT's PERCENT and no "
                      'other. A pattern states it, since equals_string needs a string '
                      'range.'],
         'domain_of': ['QuantitativeMeasure', 'QuantitativeRange'],
         'is_a': 'standard',
         'slot_uri': 'data:unit'} })
    uncertainty: Optional[Decimal] = Field(default=None, title="data uncertainty", description="""Uncertainty for a quantitative value""", json_schema_extra = { "linkml_meta": {'domain_of': ['Count', 'QuantitativeMeasure', 'QuantitativeRange'],
         'is_a': 'rdf_value',
         'slot_uri': 'data:uncertainty'} })

    @field_validator('unit')
    def pattern_unit(cls, v):
        pattern=re.compile(r"^http://qudt\.org/vocab/unit/PERCENT$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid unit format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid unit format: {v}"
            raise ValueError(err_msg)
        return v


class Text(ConfiguredBaseModel):
    """
    Class to encapsulate a textual value
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'data:Text',
         'from_schema': 'https://w3id.org/lmodel/datatype',
         'slot_usage': {'value': {'name': 'value',
                                  'range': 'string',
                                  'required': True}},
         'title': 'Text'})

    value: str = Field(default=..., title="data value", description="""simple value (a literal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Boolean', 'Count', 'QuantitativeMeasure', 'Text'],
         'is_a': 'rdf_value',
         'slot_uri': 'data:value'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Boolean.model_rebuild()
Concept.model_rebuild()
Count.model_rebuild()
QuantitativeMeasure.model_rebuild()
QuantitativeRange.model_rebuild()
Percent.model_rebuild()
PercentRange.model_rebuild()
Text.model_rebuild()
