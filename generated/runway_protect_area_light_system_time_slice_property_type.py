from dataclasses import dataclass, field
from typing import Optional

from generated.runway_protect_area_light_system_time_slice import (
    RunwayProtectAreaLightSystemTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayProtectAreaLightSystemTimeSlicePropertyType:
    runway_protect_area_light_system_time_slice: Optional[
        RunwayProtectAreaLightSystemTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "RunwayProtectAreaLightSystemTimeSlice",
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
