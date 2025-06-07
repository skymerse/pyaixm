from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.unit_of_measure_type import UnitOfMeasureType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DerivationUnitTermType(UnitOfMeasureType):
    exponent: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
