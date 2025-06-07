from dataclasses import dataclass

from generated.guidance_line_light_system_type import (
    GuidanceLineLightSystemType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GuidanceLineLightSystem(GuidanceLineLightSystemType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
