from dataclasses import dataclass, field
from typing import Optional

from generated.touch_down_lift_off_marking_time_slice import (
    TouchDownLiftOffMarkingTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TouchDownLiftOffMarkingTimeSlicePropertyType:
    touch_down_lift_off_marking_time_slice: Optional[
        TouchDownLiftOffMarkingTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "TouchDownLiftOffMarkingTimeSlice",
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
