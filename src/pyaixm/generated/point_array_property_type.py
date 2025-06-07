from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.elevated_point import ElevatedPoint
from pyaixm.generated.point_1 import Point1
from pyaixm.generated.point_2 import Point2

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PointArrayPropertyType:
    """Gml:PointArrayPropertyType is a container for an array of points.

    The elements are always contained inline in the array property,
    referencing geometry elements or arrays of geometry elements via
    XLinks is not supported.
    """

    elevated_point: Iterable[ElevatedPoint] = field(
        default_factory=list,
        metadata={
            "name": "ElevatedPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    point: Iterable[Point2] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "sequence": 1,
        },
    )
    opengis_net_gml_3_2_point: Iterable[Point1] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 1,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
