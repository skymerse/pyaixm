from dataclasses import dataclass, field
from typing import Optional

from generated.pilot_controlled_lighting_time_slice import (
    PilotControlledLightingTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PilotControlledLightingTimeSlicePropertyType:
    pilot_controlled_lighting_time_slice: Optional[
        PilotControlledLightingTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "PilotControlledLightingTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
