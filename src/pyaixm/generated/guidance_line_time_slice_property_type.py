from dataclasses import dataclass, field
from typing import Optional

from generated.guidance_line_time_slice import GuidanceLineTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GuidanceLineTimeSlicePropertyType:
    guidance_line_time_slice: Optional[GuidanceLineTimeSlice] = field(
        default=None,
        metadata={
            "name": "GuidanceLineTimeSlice",
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
