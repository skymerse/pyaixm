from dataclasses import dataclass

from generated.touch_down_lift_off_safe_area_time_slice_type import (
    TouchDownLiftOffSafeAreaTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TouchDownLiftOffSafeAreaTimeSlice(TouchDownLiftOffSafeAreaTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
