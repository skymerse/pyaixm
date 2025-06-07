from dataclasses import dataclass

from generated.runway_protect_area_type import RunwayProtectAreaType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayProtectArea(RunwayProtectAreaType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
