from dataclasses import dataclass

from generated.runway_protect_area_light_system_type import (
    RunwayProtectAreaLightSystemType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayProtectAreaLightSystem(RunwayProtectAreaLightSystemType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
