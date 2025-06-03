from dataclasses import dataclass

from generated.runway_declared_distance_value_type import (
    RunwayDeclaredDistanceValueType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayDeclaredDistanceValue(RunwayDeclaredDistanceValueType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
