from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.elevated_point import ElevatedPoint
from generated.point_2 import Point2

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PointPropertyType2(AbstractAixmpropertyType):
    class Meta:
        name = "PointPropertyType"

    elevated_point: Optional[ElevatedPoint] = field(
        default=None,
        metadata={
            "name": "ElevatedPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    point: Optional[Point2] = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
