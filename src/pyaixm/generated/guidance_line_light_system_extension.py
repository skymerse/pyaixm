from dataclasses import dataclass

from generated.guidance_line_light_system_extension_type import (
    GuidanceLineLightSystemExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class GuidanceLineLightSystemExtension(GuidanceLineLightSystemExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
