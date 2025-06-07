from dataclasses import dataclass

from pyaixm.generated.road_type import RoadType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Road(RoadType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
