from dataclasses import dataclass

from generated.point_type_2 import PointType2

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Point2(PointType2):
    class Meta:
        name = "Point"
        namespace = "http://www.aixm.aero/schema/5.1"
