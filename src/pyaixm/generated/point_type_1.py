from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_geometric_primitive_type import (
    AbstractGeometricPrimitiveType,
)
from pyaixm.generated.coordinates import Coordinates
from pyaixm.generated.pos import Pos

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PointType1(AbstractGeometricPrimitiveType):
    class Meta:
        name = "PointType"

    pos: Optional[Pos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    coordinates: Optional[Coordinates] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
