# Auto generated from datatype.yaml by pythongen.py version: 0.0.1
# Schema: datatype
#
# id: https://w3id.org/lmodel/datatype
# description: A LinkML rendering of the Datatype Ontology ("Datatypes") of the Australian Government Linked Data Working Group (AGLDWG), by Simon Cox of CSIRO. In its own words: a set of classes representing data-types. These may be used for observation results, or for the range of specific properties in other applications where scaled numbers, ranges, percents etc are required. Each class and property keeps the ontology's local name and IRI.
# license: Apache-2.0

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

from linkml_runtime.linkml_model.types import Boolean, Decimal, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, Decimal, URIorCURIE

metamodel_version = "1.12.0"
version = "2019-10-03"

# Namespaces
DATA = CurieNamespace('data', 'http://linked.data.gov.au/def/datatype/')
DATATYPE_LINKML = CurieNamespace('datatype_linkml', 'https://w3id.org/lmodel/datatype/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = DATATYPE_LINKML


# Types

# Class references



@dataclass(repr=False)
class Boolean(YAMLRoot):
    """
    Class to encapsulate a true-or-false value
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DATA["Boolean"]
    class_class_curie: ClassVar[str] = "data:Boolean"
    class_name: ClassVar[str] = "Boolean"
    class_model_uri: ClassVar[URIRef] = DATATYPE_LINKML.Boolean

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
    class_model_uri: ClassVar[URIRef] = DATATYPE_LINKML.Concept

    rdf_value: Union[str, URIorCURIE] = None
    vocabulary: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.rdf_value):
            self.MissingRequiredField("rdf_value")
        if not isinstance(self.rdf_value, URIorCURIE):
            self.rdf_value = URIorCURIE(self.rdf_value)

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
    class_model_uri: ClassVar[URIRef] = DATATYPE_LINKML.Count

    value: int = None
    uncertainty: Optional[Decimal] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, int):
            self.value = int(self.value)

        if self.uncertainty is not None and not isinstance(self.uncertainty, Decimal):
            self.uncertainty = Decimal(self.uncertainty)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantitativeMeasure(YAMLRoot):
    """
    Class to encapsulate a quantitative measure value
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DATA["QuantitativeMeasure"]
    class_class_curie: ClassVar[str] = "data:QuantitativeMeasure"
    class_name: ClassVar[str] = "QuantitativeMeasure"
    class_model_uri: ClassVar[URIRef] = DATATYPE_LINKML.QuantitativeMeasure

    value: Decimal = None
    unit: Union[str, URIorCURIE] = None
    uncertainty: Optional[Decimal] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, Decimal):
            self.value = Decimal(self.value)

        if self._is_empty(self.unit):
            self.MissingRequiredField("unit")
        if not isinstance(self.unit, URIorCURIE):
            self.unit = URIorCURIE(self.unit)

        if self.uncertainty is not None and not isinstance(self.uncertainty, Decimal):
            self.uncertainty = Decimal(self.uncertainty)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantitativeRange(YAMLRoot):
    """
    Class to encapsulate a quantitative range
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DATA["QuantitativeRange"]
    class_class_curie: ClassVar[str] = "data:QuantitativeRange"
    class_name: ClassVar[str] = "QuantitativeRange"
    class_model_uri: ClassVar[URIRef] = DATATYPE_LINKML.QuantitativeRange

    min: Decimal = None
    max: Decimal = None
    unit: Union[str, URIorCURIE] = None
    uncertainty: Optional[Decimal] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.min):
            self.MissingRequiredField("min")
        if not isinstance(self.min, Decimal):
            self.min = Decimal(self.min)

        if self._is_empty(self.max):
            self.MissingRequiredField("max")
        if not isinstance(self.max, Decimal):
            self.max = Decimal(self.max)

        if self._is_empty(self.unit):
            self.MissingRequiredField("unit")
        if not isinstance(self.unit, URIorCURIE):
            self.unit = URIorCURIE(self.unit)

        if self.uncertainty is not None and not isinstance(self.uncertainty, Decimal):
            self.uncertainty = Decimal(self.uncertainty)

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
    class_model_uri: ClassVar[URIRef] = DATATYPE_LINKML.Percent

    unit: Union[str, URIorCURIE] = None
    value: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.unit):
            self.MissingRequiredField("unit")
        if not isinstance(self.unit, URIorCURIE):
            self.unit = URIorCURIE(self.unit)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, Decimal):
            self.value = Decimal(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PercentRange(QuantitativeRange):
    """
    Class to encapsulate a quantitative range expressed as in percent values
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DATA["PercentRange"]
    class_class_curie: ClassVar[str] = "data:PercentRange"
    class_name: ClassVar[str] = "PercentRange"
    class_model_uri: ClassVar[URIRef] = DATATYPE_LINKML.PercentRange

    unit: Union[str, URIorCURIE] = None
    min: Decimal = None
    max: Decimal = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.unit):
            self.MissingRequiredField("unit")
        if not isinstance(self.unit, URIorCURIE):
            self.unit = URIorCURIE(self.unit)

        if self._is_empty(self.min):
            self.MissingRequiredField("min")
        if not isinstance(self.min, Decimal):
            self.min = Decimal(self.min)

        if self._is_empty(self.max):
            self.MissingRequiredField("max")
        if not isinstance(self.max, Decimal):
            self.max = Decimal(self.max)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Text(YAMLRoot):
    """
    Class to encapsulate a textual value
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DATA["Text"]
    class_class_curie: ClassVar[str] = "data:Text"
    class_name: ClassVar[str] = "Text"
    class_model_uri: ClassVar[URIRef] = DATATYPE_LINKML.Text

    value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.rdf_value = Slot(uri=RDF.value, name="rdf_value", curie=RDF.curie('value'),
                   model_uri=DATATYPE_LINKML.rdf_value, domain=None, range=Optional[str])

slots.value = Slot(uri=DATA.value, name="value", curie=DATA.curie('value'),
                   model_uri=DATATYPE_LINKML.value, domain=None, range=Optional[str])

slots.min = Slot(uri=DATA.min, name="min", curie=DATA.curie('min'),
                   model_uri=DATATYPE_LINKML.min, domain=None, range=Optional[Decimal])

slots.max = Slot(uri=DATA.max, name="max", curie=DATA.curie('max'),
                   model_uri=DATATYPE_LINKML.max, domain=None, range=Optional[Decimal])

slots.uncertainty = Slot(uri=DATA.uncertainty, name="uncertainty", curie=DATA.curie('uncertainty'),
                   model_uri=DATATYPE_LINKML.uncertainty, domain=None, range=Optional[Decimal])

slots.standard = Slot(uri=DATA.standard, name="standard", curie=DATA.curie('standard'),
                   model_uri=DATATYPE_LINKML.standard, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.unit = Slot(uri=DATA.unit, name="unit", curie=DATA.curie('unit'),
                   model_uri=DATATYPE_LINKML.unit, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.vocabulary = Slot(uri=DATA.vocabulary, name="vocabulary", curie=DATA.curie('vocabulary'),
                   model_uri=DATATYPE_LINKML.vocabulary, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.Boolean_value = Slot(uri=DATA.value, name="Boolean_value", curie=DATA.curie('value'),
                   model_uri=DATATYPE_LINKML.Boolean_value, domain=Boolean, range=Union[bool, Bool])

slots.Concept_rdf_value = Slot(uri=RDF.value, name="Concept_rdf_value", curie=RDF.curie('value'),
                   model_uri=DATATYPE_LINKML.Concept_rdf_value, domain=Concept, range=Union[str, URIorCURIE])

slots.Concept_vocabulary = Slot(uri=DATA.vocabulary, name="Concept_vocabulary", curie=DATA.curie('vocabulary'),
                   model_uri=DATATYPE_LINKML.Concept_vocabulary, domain=Concept, range=Union[str, URIorCURIE])

slots.Count_value = Slot(uri=DATA.value, name="Count_value", curie=DATA.curie('value'),
                   model_uri=DATATYPE_LINKML.Count_value, domain=Count, range=int)

slots.QuantitativeMeasure_value = Slot(uri=DATA.value, name="QuantitativeMeasure_value", curie=DATA.curie('value'),
                   model_uri=DATATYPE_LINKML.QuantitativeMeasure_value, domain=QuantitativeMeasure, range=Decimal)

slots.QuantitativeMeasure_unit = Slot(uri=DATA.unit, name="QuantitativeMeasure_unit", curie=DATA.curie('unit'),
                   model_uri=DATATYPE_LINKML.QuantitativeMeasure_unit, domain=QuantitativeMeasure, range=Union[str, URIorCURIE])

slots.QuantitativeRange_min = Slot(uri=DATA.min, name="QuantitativeRange_min", curie=DATA.curie('min'),
                   model_uri=DATATYPE_LINKML.QuantitativeRange_min, domain=QuantitativeRange, range=Decimal)

slots.QuantitativeRange_max = Slot(uri=DATA.max, name="QuantitativeRange_max", curie=DATA.curie('max'),
                   model_uri=DATATYPE_LINKML.QuantitativeRange_max, domain=QuantitativeRange, range=Decimal)

slots.QuantitativeRange_unit = Slot(uri=DATA.unit, name="QuantitativeRange_unit", curie=DATA.curie('unit'),
                   model_uri=DATATYPE_LINKML.QuantitativeRange_unit, domain=QuantitativeRange, range=Union[str, URIorCURIE])

slots.Percent_unit = Slot(uri=DATA.unit, name="Percent_unit", curie=DATA.curie('unit'),
                   model_uri=DATATYPE_LINKML.Percent_unit, domain=Percent, range=Union[str, URIorCURIE],
                   pattern=re.compile(r'^http://qudt\.org/vocab/unit/PERCENT$'))

slots.Percent_value = Slot(uri=DATA.value, name="Percent_value", curie=DATA.curie('value'),
                   model_uri=DATATYPE_LINKML.Percent_value, domain=Percent, range=Decimal)

slots.PercentRange_unit = Slot(uri=DATA.unit, name="PercentRange_unit", curie=DATA.curie('unit'),
                   model_uri=DATATYPE_LINKML.PercentRange_unit, domain=PercentRange, range=Union[str, URIorCURIE],
                   pattern=re.compile(r'^http://qudt\.org/vocab/unit/PERCENT$'))

slots.PercentRange_min = Slot(uri=DATA.min, name="PercentRange_min", curie=DATA.curie('min'),
                   model_uri=DATATYPE_LINKML.PercentRange_min, domain=PercentRange, range=Decimal)

slots.PercentRange_max = Slot(uri=DATA.max, name="PercentRange_max", curie=DATA.curie('max'),
                   model_uri=DATATYPE_LINKML.PercentRange_max, domain=PercentRange, range=Decimal)

slots.Text_value = Slot(uri=DATA.value, name="Text_value", curie=DATA.curie('value'),
                   model_uri=DATATYPE_LINKML.Text_value, domain=Text, range=str)
