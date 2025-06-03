from dataclasses import dataclass, field
from typing import Optional

from generated.length_type import LengthType
from generated.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SecondDefiningParameter1:
    class Meta:
        name = "SecondDefiningParameter"
        namespace = "http://www.opengis.net/gml/3.2"

    inverse_flattening: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "inverseFlattening",
            "type": "Element",
        },
    )
    semi_minor_axis: Optional[LengthType] = field(
        default=None,
        metadata={
            "name": "semiMinorAxis",
            "type": "Element",
        },
    )
    is_sphere: bool = field(
        default=True,
        metadata={
            "name": "isSphere",
            "type": "Element",
        },
    )
