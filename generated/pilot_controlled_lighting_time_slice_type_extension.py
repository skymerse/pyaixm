from dataclasses import dataclass, field
from typing import Optional

from generated.pilot_controlled_lighting_extension import (
    PilotControlledLightingExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PilotControlledLightingTimeSliceTypeExtension:
    class Meta:
        global_type = False

    pilot_controlled_lighting_extension: Optional[
        PilotControlledLightingExtension
    ] = field(
        default=None,
        metadata={
            "name": "PilotControlledLightingExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
