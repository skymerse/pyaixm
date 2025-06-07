from dataclasses import dataclass

from generated.change_over_point_time_slice_type import (
    ChangeOverPointTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ChangeOverPointTimeSlice(ChangeOverPointTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
