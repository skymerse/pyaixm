from dataclasses import dataclass

from generated.runway_declared_distance_type import RunwayDeclaredDistanceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayDeclaredDistance(RunwayDeclaredDistanceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
