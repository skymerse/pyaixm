from dataclasses import dataclass, field
from typing import Optional

from generated.visual_glide_slope_indicator_time_slice import (
    VisualGlideSlopeIndicatorTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class VisualGlideSlopeIndicatorTimeSlicePropertyType:
    visual_glide_slope_indicator_time_slice: Optional[
        VisualGlideSlopeIndicatorTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "VisualGlideSlopeIndicatorTimeSlice",
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
