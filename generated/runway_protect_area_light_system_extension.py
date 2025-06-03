from dataclasses import dataclass

from generated.runway_protect_area_light_system_extension_type import (
    RunwayProtectAreaLightSystemExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class RunwayProtectAreaLightSystemExtension(
    RunwayProtectAreaLightSystemExtensionType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
