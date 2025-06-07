from dataclasses import dataclass, field
from typing import Optional

from generated.guidance_line_marking_time_slice import (
    GuidanceLineMarkingTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GuidanceLineMarkingTimeSlicePropertyType:
    guidance_line_marking_time_slice: Optional[
        GuidanceLineMarkingTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "GuidanceLineMarkingTimeSlice",
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
