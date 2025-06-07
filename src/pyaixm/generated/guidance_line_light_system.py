from dataclasses import dataclass

from pyaixm.generated.guidance_line_light_system_type import (
    GuidanceLineLightSystemType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GuidanceLineLightSystem(GuidanceLineLightSystemType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
