from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.conversion_to_preferred_unit import ConversionToPreferredUnit
from generated.derivation_unit_term import DerivationUnitTerm
from generated.rough_conversion_to_preferred_unit import (
    RoughConversionToPreferredUnit,
)
from generated.unit_definition_type import UnitDefinitionType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ConventionalUnitType(UnitDefinitionType):
    conversion_to_preferred_unit: Optional[ConversionToPreferredUnit] = field(
        default=None,
        metadata={
            "name": "conversionToPreferredUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    rough_conversion_to_preferred_unit: Optional[
        RoughConversionToPreferredUnit
    ] = field(
        default=None,
        metadata={
            "name": "roughConversionToPreferredUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    derivation_unit_term: Iterable[DerivationUnitTerm] = field(
        default_factory=list,
        metadata={
            "name": "derivationUnitTerm",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
