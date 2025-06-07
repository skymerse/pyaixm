from dataclasses import dataclass, field
from typing import Optional

from generated.guidance_line_light_system_time_slice import (
    GuidanceLineLightSystemTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GuidanceLineLightSystemTimeSlicePropertyType:
    guidance_line_light_system_time_slice: Optional[
        GuidanceLineLightSystemTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "GuidanceLineLightSystemTimeSlice",
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
