from dataclasses import dataclass

from generated.ground_light_system_extension_type import (
    GroundLightSystemExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class GroundLightSystemExtension(GroundLightSystemExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
