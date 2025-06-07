from dataclasses import dataclass

from pyaixm.generated.touch_down_lift_off_light_system_time_slice_type import (
    TouchDownLiftOffLightSystemTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TouchDownLiftOffLightSystemTimeSlice(
    TouchDownLiftOffLightSystemTimeSliceType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
