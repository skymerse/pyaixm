from dataclasses import dataclass

from generated.touch_down_lift_off_marking_time_slice_type import (
    TouchDownLiftOffMarkingTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TouchDownLiftOffMarkingTimeSlice(TouchDownLiftOffMarkingTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
