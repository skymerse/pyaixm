from dataclasses import dataclass

from generated.non_movement_area_time_slice_type import (
    NonMovementAreaTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NonMovementAreaTimeSlice(NonMovementAreaTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
