from dataclasses import dataclass

from generated.deicing_area_marking_time_slice_type import (
    DeicingAreaMarkingTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DeicingAreaMarkingTimeSlice(DeicingAreaMarkingTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
