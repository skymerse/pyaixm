from dataclasses import dataclass

from generated.pilot_controlled_lighting_extension_type import (
    PilotControlledLightingExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class PilotControlledLightingExtension(PilotControlledLightingExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
