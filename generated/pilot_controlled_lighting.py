from dataclasses import dataclass

from generated.pilot_controlled_lighting_type import (
    PilotControlledLightingType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PilotControlledLighting(PilotControlledLightingType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
