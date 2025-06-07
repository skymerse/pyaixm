from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.touch_down_lift_off_light_system_time_slice import (
    TouchDownLiftOffLightSystemTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TouchDownLiftOffLightSystemTimeSlicePropertyType:
    touch_down_lift_off_light_system_time_slice: Optional[
        TouchDownLiftOffLightSystemTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "TouchDownLiftOffLightSystemTimeSlice",
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
