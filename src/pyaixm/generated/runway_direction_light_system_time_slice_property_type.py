from dataclasses import dataclass, field
from typing import Optional

from generated.runway_direction_light_system_time_slice import (
    RunwayDirectionLightSystemTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayDirectionLightSystemTimeSlicePropertyType:
    runway_direction_light_system_time_slice: Optional[
        RunwayDirectionLightSystemTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "RunwayDirectionLightSystemTimeSlice",
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
