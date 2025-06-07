from dataclasses import dataclass

from pyaixm.generated.runway_direction_light_system_type import (
    RunwayDirectionLightSystemType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayDirectionLightSystem(RunwayDirectionLightSystemType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
