from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_general_operation_parameter_property_type import (
    GeneralOperationParameter,
    IncludesParameter,
    Parameter,
    UsesParameter,
)
from generated.formula import Formula
from generated.formula_citation import FormulaCitation
from generated.identified_object_type import IdentifiedObjectType
from generated.method_formula import MethodFormula
from generated.source_dimensions import SourceDimensions
from generated.target_dimensions import TargetDimensions

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class OperationMethodType(IdentifiedObjectType):
    formula_citation: Optional[FormulaCitation] = field(
        default=None,
        metadata={
            "name": "formulaCitation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    method_formula: Optional[MethodFormula] = field(
        default=None,
        metadata={
            "name": "methodFormula",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    formula: Optional[Formula] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    source_dimensions: Optional[SourceDimensions] = field(
        default=None,
        metadata={
            "name": "sourceDimensions",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    target_dimensions: Optional[TargetDimensions] = field(
        default=None,
        metadata={
            "name": "targetDimensions",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    uses_parameter: Iterable[UsesParameter] = field(
        default_factory=list,
        metadata={
            "name": "usesParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    general_operation_parameter: Iterable[GeneralOperationParameter] = field(
        default_factory=list,
        metadata={
            "name": "generalOperationParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    includes_parameter: Iterable[IncludesParameter] = field(
        default_factory=list,
        metadata={
            "name": "includesParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    parameter: Iterable[Parameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
