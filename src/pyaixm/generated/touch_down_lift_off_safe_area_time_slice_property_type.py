from dataclasses import dataclass, field
from typing import Optional

from generated.touch_down_lift_off_safe_area_time_slice import (
    TouchDownLiftOffSafeAreaTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TouchDownLiftOffSafeAreaTimeSlicePropertyType:
    touch_down_lift_off_safe_area_time_slice: Optional[
        TouchDownLiftOffSafeAreaTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "TouchDownLiftOffSafeAreaTimeSlice",
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
