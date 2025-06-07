from dataclasses import dataclass

from pyaixm.generated.touch_down_lift_off_time_slice_type import (
    TouchDownLiftOffTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TouchDownLiftOffTimeSlice(TouchDownLiftOffTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
