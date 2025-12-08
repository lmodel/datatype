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


metamodel_version = "None"
version = "None"


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

    @model_serializer(mode='wrap', when_used='unless-none')
    def treat_empty_lists_as_none(
            self, handler: SerializerFunctionWrapHandler,
            info: SerializationInfo) -> dict[str, Any]:
        if info.exclude_none:
            _instance = self.model_copy()
            for field, field_info in type(_instance).model_fields.items():
                if getattr(_instance, field) == [] and not(
                        field_info.is_required()):
                    setattr(_instance, field, None)
        else:
            _instance = self
        return handler(_instance, info)



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


linkml_meta = LinkMLMeta({'default_prefix': 'data',
     'default_range': 'string',
     'description': 'A set of classes representing data-types. These may be used '
                    'for observation results, or for the range of specific '
                    'properties in other applications where scaled numbers, '
                    'ranges, percents etc are required.\n'
                    'LinkML rendering of http://linked.data.gov.au/def/datatype',
     'id': 'https://w3id.org/lmodel/datatype',
     'imports': ['linkml:types'],
     'license': 'CC0-1.0',
     'name': 'datatype',
     'notes': ['Originally developed for use as the value of an observation result '
               '(sosa:hasResult) in the context of the TERN-plot ontology. '
               'However, objects from these classes may appear in many contexts.'],
     'prefixes': {'NCIT': {'prefix_prefix': 'NCIT',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/NCIT_'},
                  'OBCS': {'prefix_prefix': 'OBCS',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/OBCS_'},
                  'STATO': {'prefix_prefix': 'STATO',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/STATO_'},
                  'UO': {'prefix_prefix': 'UO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/UO_'},
                  'data': {'prefix_prefix': 'data',
                           'prefix_reference': 'http://linked.data.gov.au/def/datatype/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'owl': {'prefix_prefix': 'owl',
                          'prefix_reference': 'http://www.w3.org/2002/07/owl#'},
                  'prov': {'prefix_prefix': 'prov',
                           'prefix_reference': 'http://www.w3.org/ns/prov#'},
                  'qudt': {'prefix_prefix': 'qudt',
                           'prefix_reference': 'http://qudt.org/schema/qudt/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'},
                  'rdfs': {'prefix_prefix': 'rdfs',
                           'prefix_reference': 'http://www.w3.org/2000/01/rdf-schema#'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'},
                  'wikidata': {'prefix_prefix': 'wikidata',
                               'prefix_reference': 'https://www.wikidata.org/wiki/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['http://linked.data.gov.au/def/datatype'],
     'source_file': 'src/datatype/schema/datatype.yaml',
     'title': 'AGLDWG Datatype Ontology (LinkML rendering)',
     'types': {'concept value': {'base': 'str',
                                 'description': 'Idea or notion; a unit of thought',
                                 'from_schema': 'https://w3id.org/lmodel/datatype',
                                 'name': 'concept value',
                                 'typeof': 'string value',
                                 'uri': 'skos:Concept'},
               'data value': {'base': 'str',
                              'description': 'simple value (a literal)',
                              'from_schema': 'https://w3id.org/lmodel/datatype',
                              'name': 'data value',
                              'typeof': 'string value',
                              'uri': 'rdf:value'},
               'decimal value': {'base': 'float',
                                 'description': 'Generic decimal value used for '
                                                'quantitative measures',
                                 'from_schema': 'https://w3id.org/lmodel/datatype',
                                 'name': 'decimal value',
                                 'uri': 'xsd:decimal'},
               'integer value': {'base': 'int',
                                 'description': 'Integer count value',
                                 'from_schema': 'https://w3id.org/lmodel/datatype',
                                 'name': 'integer value',
                                 'uri': 'xsd:integer'},
               'percent value': {'base': 'float',
                                 'description': 'Percentage value',
                                 'from_schema': 'https://w3id.org/lmodel/datatype',
                                 'name': 'percent value',
                                 'typeof': 'double',
                                 'uri': 'UO:0000187'},
               'string value': {'base': 'str',
                                'description': 'Generic string value',
                                'from_schema': 'https://w3id.org/lmodel/datatype',
                                'name': 'string value',
                                'uri': 'xsd:string'},
               'unit value': {'base': 'str',
                              'description': 'Unit of measure value',
                              'exact_mappings': ['qudt:Unit'],
                              'from_schema': 'https://w3id.org/lmodel/datatype',
                              'id_prefixes': ['UO'],
                              'name': 'unit value',
                              'typeof': 'string value',
                              'uri': 'UO:0000000'}}} )


class Text(ConfiguredBaseModel):
    """
    Class to encapsulate a textual value
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['NCIT:C25704',
                            'schema:Text',
                            'wikidata:Q234460',
                            'wikidata:Q1145976'],
         'from_schema': 'https://w3id.org/lmodel/datatype',
         'slot_usage': {'value': {'name': 'value',
                                  'range': 'string value',
                                  'required': True,
                                  'slot_uri': 'xsd:string'}}})

    value: str = Field(default=..., description="""simple value (a literal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Text', 'Boolean', 'Concept', 'Count', 'Quantitative Measure'],
         'exact_mappings': ['schema:Value'],
         'narrow_mappings': ['NCIT:C25712', 'prov:Value'],
         'see_also': ['http://linked.data.gov.au/def/datatype/Value'],
         'slot_uri': 'xsd:string'} })


class Boolean(ConfiguredBaseModel):
    """
    Class to encapsulate a true-or-false value
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['wikidata:Q3269980'],
         'exact_mappings': ['NCIT:C45254', 'wikidata:Q520777'],
         'from_schema': 'https://w3id.org/lmodel/datatype',
         'see_also': ['http://linked.data.gov.au/def/datatype/Boolean'],
         'slot_usage': {'value': {'name': 'value',
                                  'range': 'boolean',
                                  'required': True,
                                  'slot_uri': 'xsd:boolean'}}})

    value: bool = Field(default=..., description="""simple value (a literal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Text', 'Boolean', 'Concept', 'Count', 'Quantitative Measure'],
         'exact_mappings': ['schema:Value'],
         'narrow_mappings': ['NCIT:C25712', 'prov:Value'],
         'see_also': ['http://linked.data.gov.au/def/datatype/Value'],
         'slot_uri': 'xsd:boolean'} })


class Concept(ConfiguredBaseModel):
    """
    Class to encapsulate a classifier, usually a values from a controlled vocabulary
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['NCIT:C45728', 'skos:Concept', 'wikidata:Q151885'],
         'from_schema': 'https://w3id.org/lmodel/datatype',
         'see_also': ['http://linked.data.gov.au/def/datatype/Concept'],
         'slot_usage': {'value': {'name': 'value',
                                  'range': 'concept value',
                                  'required': True},
                        'vocabulary': {'name': 'vocabulary', 'required': True}}})

    value: str = Field(default=..., description="""simple value (a literal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Text', 'Boolean', 'Concept', 'Count', 'Quantitative Measure'],
         'exact_mappings': ['schema:Value'],
         'narrow_mappings': ['NCIT:C25712', 'prov:Value'],
         'see_also': ['http://linked.data.gov.au/def/datatype/Value']} })
    vocabulary: str = Field(default=..., description="""controlled vocabulary, taxonomy etc""", json_schema_extra = { "linkml_meta": {'broad_mappings': ['skos:ConceptScheme', 'skos:Collection', 'owl:Ontology'],
         'domain_of': ['Concept'],
         'exact_mappings': ['skos:Concept'],
         'is_a': 'standard',
         'see_also': ['http://linked.data.gov.au/def/datatype/Vocabulary']} })


class Count(ConfiguredBaseModel):
    """
    Class to encapsulate an integer value
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['NCIT:Q1520033', 'wikidata:Q1520033'],
         'from_schema': 'https://w3id.org/lmodel/datatype',
         'related_mappings': ['NCIT:C25463', 'wikidata:Q729138'],
         'see_also': ['http://linked.data.gov.au/def/datatype/Count'],
         'slot_usage': {'value': {'name': 'value',
                                  'range': 'integer value',
                                  'required': True}}})

    value: int = Field(default=..., description="""simple value (a literal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Text', 'Boolean', 'Concept', 'Count', 'Quantitative Measure'],
         'exact_mappings': ['schema:Value'],
         'narrow_mappings': ['NCIT:C25712', 'prov:Value'],
         'see_also': ['http://linked.data.gov.au/def/datatype/Value']} })
    uncertainty: Optional[float] = Field(default=None, description="""Uncertainty for a quantitative value""", json_schema_extra = { "linkml_meta": {'aliases': ['data uncertainty'],
         'close_mappings': ['wikidata:Q1403517'],
         'domain_of': ['Count', 'Quantitative Measure', 'Quantitative Range'],
         'is_a': 'value',
         'narrow_mappings': ['OBCS:0000340'],
         'see_also': ['http://linked.data.gov.au/def/datatype/Uncertainty']} })


class QuantitativeMeasure(ConfiguredBaseModel):
    """
    Class to encapsulate a quantitative measure value
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/datatype',
         'related_mappings': ['schema:QuantitativeValue', 'wikidata:Q309314'],
         'see_also': ['http://linked.data.gov.au/def/datatype/QuantitativeMeasure'],
         'slot_usage': {'unit': {'name': 'unit', 'required': True},
                        'value': {'name': 'value',
                                  'range': 'decimal value',
                                  'required': True}}})

    value: float = Field(default=..., description="""simple value (a literal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Text', 'Boolean', 'Concept', 'Count', 'Quantitative Measure'],
         'exact_mappings': ['schema:Value'],
         'narrow_mappings': ['NCIT:C25712', 'prov:Value'],
         'see_also': ['http://linked.data.gov.au/def/datatype/Value']} })
    unit: str = Field(default=..., description="""Measurement scale""", json_schema_extra = { "linkml_meta": {'aliases': ['unit of measure'],
         'domain_of': ['Quantitative Measure', 'Quantitative Range'],
         'is_a': 'standard',
         'see_also': ['http://linked.data.gov.au/def/datatype/Unit']} })
    uncertainty: Optional[float] = Field(default=None, description="""Uncertainty for a quantitative value""", json_schema_extra = { "linkml_meta": {'aliases': ['data uncertainty'],
         'close_mappings': ['wikidata:Q1403517'],
         'domain_of': ['Count', 'Quantitative Measure', 'Quantitative Range'],
         'is_a': 'value',
         'narrow_mappings': ['OBCS:0000340'],
         'see_also': ['http://linked.data.gov.au/def/datatype/Uncertainty']} })
    standard: Optional[str] = Field(default=None, description="""Measurement standard, scale, uom, reference system, controlled vocabulary, taxonomy etc""", json_schema_extra = { "linkml_meta": {'aliases': ['data standard'],
         'domain_of': ['Quantitative Measure'],
         'exact_mappings': ['NCIT:C14298', 'wikidata:Q1271511'],
         'see_also': ['http://linked.data.gov.au/def/datatype/Standard']} })


class QuantitativeRange(ConfiguredBaseModel):
    """
    Class to encapsulate a quantitative range
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/datatype',
         'related_mappings': ['wikidata:Q1165839'],
         'see_also': ['http://linked.data.gov.au/def/datatype/QuantitativeRange'],
         'slot_usage': {'max': {'name': 'max',
                                'range': 'decimal value',
                                'required': True},
                        'min': {'name': 'min',
                                'range': 'decimal value',
                                'required': True},
                        'unit': {'name': 'unit', 'required': True}}})

    min: float = Field(default=..., description="""Minimum value of range""", json_schema_extra = { "linkml_meta": {'aliases': ['data minimum'],
         'close_mappings': ['wikidata:Q10585806'],
         'domain_of': ['Quantitative Range'],
         'is_a': 'value',
         'see_also': ['http://linked.data.gov.au/def/datatype/Min']} })
    max: float = Field(default=..., description="""Maximum value of a range""", json_schema_extra = { "linkml_meta": {'aliases': ['data maximum'],
         'close_mappings': ['wikidata:Q10578722', 'STATO:0000666', 'STATO:0000151'],
         'domain_of': ['Quantitative Range'],
         'is_a': 'value',
         'see_also': ['http://linked.data.gov.au/def/datatype/Max']} })
    unit: str = Field(default=..., description="""Measurement scale""", json_schema_extra = { "linkml_meta": {'aliases': ['unit of measure'],
         'domain_of': ['Quantitative Measure', 'Quantitative Range'],
         'is_a': 'standard',
         'see_also': ['http://linked.data.gov.au/def/datatype/Unit']} })
    uncertainty: Optional[float] = Field(default=None, description="""Uncertainty for a quantitative value""", json_schema_extra = { "linkml_meta": {'aliases': ['data uncertainty'],
         'close_mappings': ['wikidata:Q1403517'],
         'domain_of': ['Count', 'Quantitative Measure', 'Quantitative Range'],
         'is_a': 'value',
         'narrow_mappings': ['OBCS:0000340'],
         'see_also': ['http://linked.data.gov.au/def/datatype/Uncertainty']} })


class Percent(QuantitativeMeasure):
    """
    Class to encapsulate a quantitative measure expressed as a percent value
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['NCIT:C48570', 'UO:0000187', 'wikidata:Q11229'],
         'from_schema': 'https://w3id.org/lmodel/datatype',
         'see_also': ['http://linked.data.gov.au/def/datatype/Percent'],
         'slot_usage': {'unit': {'broad_mappings': ['wikidata:Q1196827'],
                                 'name': 'unit',
                                 'range': 'percent value',
                                 'slot_uri': 'qudt:PERCENT'}}})

    value: float = Field(default=..., description="""simple value (a literal)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Text', 'Boolean', 'Concept', 'Count', 'Quantitative Measure'],
         'exact_mappings': ['schema:Value'],
         'narrow_mappings': ['NCIT:C25712', 'prov:Value'],
         'see_also': ['http://linked.data.gov.au/def/datatype/Value']} })
    unit: float = Field(default=..., description="""Measurement scale""", json_schema_extra = { "linkml_meta": {'aliases': ['unit of measure'],
         'broad_mappings': ['wikidata:Q1196827'],
         'domain_of': ['Quantitative Measure', 'Quantitative Range'],
         'is_a': 'standard',
         'see_also': ['http://linked.data.gov.au/def/datatype/Unit'],
         'slot_uri': 'qudt:PERCENT'} })
    uncertainty: Optional[float] = Field(default=None, description="""Uncertainty for a quantitative value""", json_schema_extra = { "linkml_meta": {'aliases': ['data uncertainty'],
         'close_mappings': ['wikidata:Q1403517'],
         'domain_of': ['Count', 'Quantitative Measure', 'Quantitative Range'],
         'is_a': 'value',
         'narrow_mappings': ['OBCS:0000340'],
         'see_also': ['http://linked.data.gov.au/def/datatype/Uncertainty']} })
    standard: Optional[str] = Field(default=None, description="""Measurement standard, scale, uom, reference system, controlled vocabulary, taxonomy etc""", json_schema_extra = { "linkml_meta": {'aliases': ['data standard'],
         'domain_of': ['Quantitative Measure'],
         'exact_mappings': ['NCIT:C14298', 'wikidata:Q1271511'],
         'see_also': ['http://linked.data.gov.au/def/datatype/Standard']} })


class PercentRange(QuantitativeRange):
    """
    Class to encapsulate a quantitative range expressed as in percent values
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/datatype',
         'see_also': ['http://linked.data.gov.au/def/datatype/PercentRange'],
         'slot_usage': {'unit': {'name': 'unit',
                                 'range': 'percent value',
                                 'slot_uri': 'qudt:PERCENT'}}})

    min: float = Field(default=..., description="""Minimum value of range""", json_schema_extra = { "linkml_meta": {'aliases': ['data minimum'],
         'close_mappings': ['wikidata:Q10585806'],
         'domain_of': ['Quantitative Range'],
         'is_a': 'value',
         'see_also': ['http://linked.data.gov.au/def/datatype/Min']} })
    max: float = Field(default=..., description="""Maximum value of a range""", json_schema_extra = { "linkml_meta": {'aliases': ['data maximum'],
         'close_mappings': ['wikidata:Q10578722', 'STATO:0000666', 'STATO:0000151'],
         'domain_of': ['Quantitative Range'],
         'is_a': 'value',
         'see_also': ['http://linked.data.gov.au/def/datatype/Max']} })
    unit: float = Field(default=..., description="""Measurement scale""", json_schema_extra = { "linkml_meta": {'aliases': ['unit of measure'],
         'domain_of': ['Quantitative Measure', 'Quantitative Range'],
         'is_a': 'standard',
         'see_also': ['http://linked.data.gov.au/def/datatype/Unit'],
         'slot_uri': 'qudt:PERCENT'} })
    uncertainty: Optional[float] = Field(default=None, description="""Uncertainty for a quantitative value""", json_schema_extra = { "linkml_meta": {'aliases': ['data uncertainty'],
         'close_mappings': ['wikidata:Q1403517'],
         'domain_of': ['Count', 'Quantitative Measure', 'Quantitative Range'],
         'is_a': 'value',
         'narrow_mappings': ['OBCS:0000340'],
         'see_also': ['http://linked.data.gov.au/def/datatype/Uncertainty']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Text.model_rebuild()
Boolean.model_rebuild()
Concept.model_rebuild()
Count.model_rebuild()
QuantitativeMeasure.model_rebuild()
QuantitativeRange.model_rebuild()
Percent.model_rebuild()
PercentRange.model_rebuild()
