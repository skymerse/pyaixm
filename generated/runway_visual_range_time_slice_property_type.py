from dataclasses import dataclass, field
from typing import Optional

from generated.runway_visual_range_time_slice import RunwayVisualRangeTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayVisualRangeTimeSlicePropertyType:
    runway_visual_range_time_slice: Optional[RunwayVisualRangeTimeSlice] = (
        field(
            default=None,
            metadata={
                "name": "RunwayVisualRangeTimeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "required": True,
            },
        )
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
