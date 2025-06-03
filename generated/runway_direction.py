from dataclasses import dataclass

from generated.runway_direction_type import RunwayDirectionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayDirection(RunwayDirectionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
