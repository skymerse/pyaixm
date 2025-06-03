from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.derivation_unit_term import DerivationUnitTerm
from generated.unit_definition_type import UnitDefinitionType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DerivedUnitType(UnitDefinitionType):
    derivation_unit_term: Iterable[DerivationUnitTerm] = field(
        default_factory=list,
        metadata={
            "name": "derivationUnitTerm",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )
