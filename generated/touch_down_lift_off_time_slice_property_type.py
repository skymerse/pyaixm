from dataclasses import dataclass, field
from typing import Optional

from generated.touch_down_lift_off_time_slice import TouchDownLiftOffTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TouchDownLiftOffTimeSlicePropertyType:
    touch_down_lift_off_time_slice: Optional[TouchDownLiftOffTimeSlice] = (
        field(
            default=None,
            metadata={
                "name": "TouchDownLiftOffTimeSlice",
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
