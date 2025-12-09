# Auto generated from datatype.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-12-10T00:08:17
# Schema: datatype
#
# id: https://w3id.org/lmodel/datatype
# description: LinkML schema of AGLDWG Datatypes (http://linked.data.gov.au/def/datatype).
#
#   A set of classes representing data-types. These may be used for observation
#   results, or for the range of specific properties in other applications where
#   scaled numbers, ranges, percents, etc, are required.
#
#   History Note: Originally developed for use as the value of an observation
#   result (sosa:hasResult) in the context of the TERN-plot ontology. However,
#   objects from these classes may appear in many contexts.
# license: http://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Double, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE

metamodel_version = "1.7.0"
version = None

# Namespaces
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OBCS = CurieNamespace('OBCS', 'http://purl.obolibrary.org/obo/OBCS_')
STATO = CurieNamespace('STATO', 'http://purl.obolibrary.org/obo/STATO_')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
DATA = CurieNamespace('data', 'http://linked.data.gov.au/def/datatype/')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
QUDT = CurieNamespace('qudt', 'http://qudt.org/schema/qudt/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
WIKIDATA = CurieNamespace('wikidata', 'https://www.wikidata.org/wiki/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = DATA


# Types
class DecimalValue(float):
    """ Generic decimal value used for quantitative measures """
    type_class_uri = XSD["decimal"]
    type_class_curie = "xsd:decimal"
    type_name = "decimal value"
    type_model_uri = DATA.DecimalValue


class IntegerValue(int):
    """ Integer count value """
    type_class_uri = XSD["integer"]
    type_class_curie = "xsd:integer"
    type_name = "integer value"
    type_model_uri = DATA.IntegerValue


class StringValue(str):
    """ Generic string value """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "string value"
    type_model_uri = DATA.StringValue


class PercentValue(Double):
    """ Percentage value """
    type_class_uri = UO["0000187"]
    type_class_curie = "UO:0000187"
    type_name = "percent value"
    type_model_uri = DATA.PercentValue


class ConceptValue(StringValue):
    """ Idea or notion; a unit of thought """
    type_class_uri = SKOS["Concept"]
    type_class_curie = "skos:Concept"
    type_name = "concept value"
    type_model_uri = DATA.ConceptValue


class DataValue(StringValue):
    """ simple value (a literal) """
    type_class_uri = XSD["nonNegativeInteger"]
    type_class_curie = "xsd:nonNegativeInteger"
    type_name = "data value"
    type_model_uri = DATA.DataValue


class UnitValue(StringValue):
    """ Unit of measure value """
    type_class_uri = UO["0000000"]
    type_class_curie = "UO:0000000"
    type_name = "unit value"
    type_model_uri = DATA.UnitValue


# Class references



@dataclass(repr=False)
class Text(YAMLRoot):
    """
    Class to encapsulate a textual value
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DATA["Text"]
    class_class_curie: ClassVar[str] = "data:Text"
    class_name: ClassVar[str] = "Text"
    class_model_uri: ClassVar[URIRef] = DATA.Text

    value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Boolean(YAMLRoot):
    """
    Class to encapsulate a true-or-false value
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DATA["Boolean"]
    class_class_curie: ClassVar[str] = "data:Boolean"
    class_name: ClassVar[str] = "Boolean"
    class_model_uri: ClassVar[URIRef] = DATA.Boolean

    value: Union[bool, Bool] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, Bool):
            self.value = Bool(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Concept(YAMLRoot):
    """
    Class to encapsulate a classifier, usually a values from a controlled vocabulary
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DATA["Concept"]
    class_class_curie: ClassVar[str] = "data:Concept"
    class_name: ClassVar[str] = "Concept"
    class_model_uri: ClassVar[URIRef] = DATA.Concept

    value: Union[str, ConceptValue] = None
    vocabulary: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, ConceptValue):
            self.value = ConceptValue(self.value)

        if self._is_empty(self.vocabulary):
            self.MissingRequiredField("vocabulary")
        if not isinstance(self.vocabulary, URIorCURIE):
            self.vocabulary = URIorCURIE(self.vocabulary)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Count(YAMLRoot):
    """
    Class to encapsulate an integer value
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DATA["Count"]
    class_class_curie: ClassVar[str] = "data:Count"
    class_name: ClassVar[str] = "Count"
    class_model_uri: ClassVar[URIRef] = DATA.Count

    value: int = None
    uncertainty: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, int):
            self.value = int(self.value)

        if self.uncertainty is not None and not isinstance(self.uncertainty, float):
            self.uncertainty = float(self.uncertainty)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantitativeMeasure(YAMLRoot):
    """
    Class to encapsulate a quantitative measure value
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DATA["QuantitativeMeasure"]
    class_class_curie: ClassVar[str] = "data:QuantitativeMeasure"
    class_name: ClassVar[str] = "Quantitative Measure"
    class_model_uri: ClassVar[URIRef] = DATA.QuantitativeMeasure

    value: float = None
    unit: Union[str, UnitValue] = None
    uncertainty: Optional[float] = None
    standard: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, float):
            self.value = float(self.value)

        if self._is_empty(self.unit):
            self.MissingRequiredField("unit")
        if not isinstance(self.unit, UnitValue):
            self.unit = UnitValue(self.unit)

        if self.uncertainty is not None and not isinstance(self.uncertainty, float):
            self.uncertainty = float(self.uncertainty)

        if self.standard is not None and not isinstance(self.standard, URIorCURIE):
            self.standard = URIorCURIE(self.standard)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantitativeRange(YAMLRoot):
    """
    Class to encapsulate a quantitative range
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DATA["QuantitativeRange"]
    class_class_curie: ClassVar[str] = "data:QuantitativeRange"
    class_name: ClassVar[str] = "Quantitative Range"
    class_model_uri: ClassVar[URIRef] = DATA.QuantitativeRange

    min: float = None
    max: float = None
    unit: Union[str, UnitValue] = None
    uncertainty: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.min):
            self.MissingRequiredField("min")
        if not isinstance(self.min, float):
            self.min = float(self.min)

        if self._is_empty(self.max):
            self.MissingRequiredField("max")
        if not isinstance(self.max, float):
            self.max = float(self.max)

        if self._is_empty(self.unit):
            self.MissingRequiredField("unit")
        if not isinstance(self.unit, UnitValue):
            self.unit = UnitValue(self.unit)

        if self.uncertainty is not None and not isinstance(self.uncertainty, float):
            self.uncertainty = float(self.uncertainty)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Percent(QuantitativeMeasure):
    """
    Class to encapsulate a quantitative measure expressed as a percent value
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DATA["Percent"]
    class_class_curie: ClassVar[str] = "data:Percent"
    class_name: ClassVar[str] = "Percent"
    class_model_uri: ClassVar[URIRef] = DATA.Percent

    value: float = None
    unit: Union[float, PercentValue] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.unit):
            self.MissingRequiredField("unit")
        if not isinstance(self.unit, PercentValue):
            self.unit = PercentValue(self.unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PercentRange(QuantitativeRange):
    """
    Class to encapsulate a quantitative range expressed as in percent values
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DATA["PercentRange"]
    class_class_curie: ClassVar[str] = "data:PercentRange"
    class_name: ClassVar[str] = "Percent Range"
    class_model_uri: ClassVar[URIRef] = DATA.PercentRange

    min: float = None
    max: float = None
    unit: Union[float, PercentValue] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.unit):
            self.MissingRequiredField("unit")
        if not isinstance(self.unit, PercentValue):
            self.unit = PercentValue(self.unit)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.value = Slot(uri=DATA.value, name="value", curie=DATA.curie('value'),
                   model_uri=DATA.value, domain=None, range=Optional[Union[str, DataValue]])

slots.min = Slot(uri=DATA.min, name="min", curie=DATA.curie('min'),
                   model_uri=DATA.min, domain=None, range=Optional[float])

slots.max = Slot(uri=DATA.max, name="max", curie=DATA.curie('max'),
                   model_uri=DATA.max, domain=None, range=Optional[float])

slots.uncertainty = Slot(uri=DATA.uncertainty, name="uncertainty", curie=DATA.curie('uncertainty'),
                   model_uri=DATA.uncertainty, domain=None, range=Optional[float])

slots.standard = Slot(uri=DATA.standard, name="standard", curie=DATA.curie('standard'),
                   model_uri=DATA.standard, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.unit = Slot(uri=DATA.unit, name="unit", curie=DATA.curie('unit'),
                   model_uri=DATA.unit, domain=None, range=Optional[Union[str, UnitValue]])

slots.vocabulary = Slot(uri=DATA.vocabulary, name="vocabulary", curie=DATA.curie('vocabulary'),
                   model_uri=DATA.vocabulary, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.Text_value = Slot(uri=XSD.string, name="Text_value", curie=XSD.curie('string'),
                   model_uri=DATA.Text_value, domain=Text, range=str)

slots.Boolean_value = Slot(uri=XSD.boolean, name="Boolean_value", curie=XSD.curie('boolean'),
                   model_uri=DATA.Boolean_value, domain=Boolean, range=Union[bool, Bool])

slots.Concept_value = Slot(uri=DATA.value, name="Concept_value", curie=DATA.curie('value'),
                   model_uri=DATA.Concept_value, domain=Concept, range=Union[str, ConceptValue])

slots.Concept_vocabulary = Slot(uri=DATA.vocabulary, name="Concept_vocabulary", curie=DATA.curie('vocabulary'),
                   model_uri=DATA.Concept_vocabulary, domain=Concept, range=Union[str, URIorCURIE])

slots.Count_value = Slot(uri=DATA.value, name="Count_value", curie=DATA.curie('value'),
                   model_uri=DATA.Count_value, domain=Count, range=int)

slots.Quantitative_Measure_unit = Slot(uri=DATA.unit, name="Quantitative Measure_unit", curie=DATA.curie('unit'),
                   model_uri=DATA.Quantitative_Measure_unit, domain=QuantitativeMeasure, range=Union[str, UnitValue])

slots.Quantitative_Measure_value = Slot(uri=DATA.value, name="Quantitative Measure_value", curie=DATA.curie('value'),
                   model_uri=DATA.Quantitative_Measure_value, domain=QuantitativeMeasure, range=float)

slots.Quantitative_Range_unit = Slot(uri=DATA.unit, name="Quantitative Range_unit", curie=DATA.curie('unit'),
                   model_uri=DATA.Quantitative_Range_unit, domain=QuantitativeRange, range=Union[str, UnitValue])

slots.Quantitative_Range_min = Slot(uri=DATA.min, name="Quantitative Range_min", curie=DATA.curie('min'),
                   model_uri=DATA.Quantitative_Range_min, domain=QuantitativeRange, range=float)

slots.Quantitative_Range_max = Slot(uri=DATA.max, name="Quantitative Range_max", curie=DATA.curie('max'),
                   model_uri=DATA.Quantitative_Range_max, domain=QuantitativeRange, range=float)

slots.Percent_unit = Slot(uri=QUDT.PERCENT, name="Percent_unit", curie=QUDT.curie('PERCENT'),
                   model_uri=DATA.Percent_unit, domain=Percent, range=Union[float, PercentValue])

slots.Percent_Range_unit = Slot(uri=QUDT.PERCENT, name="Percent Range_unit", curie=QUDT.curie('PERCENT'),
                   model_uri=DATA.Percent_Range_unit, domain=PercentRange, range=Union[float, PercentValue])
