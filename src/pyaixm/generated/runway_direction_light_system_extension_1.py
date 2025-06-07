from dataclasses import dataclass

from generated.runway_direction_light_system_extension_type_1 import (
    RunwayDirectionLightSystemExtensionType1,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class RunwayDirectionLightSystemExtension1(
    RunwayDirectionLightSystemExtensionType1
):
    class Meta:
        name = "RunwayDirectionLightSystemExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
