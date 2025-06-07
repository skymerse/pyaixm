from dataclasses import dataclass

from generated.marking_buoy_time_slice_type import MarkingBuoyTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class MarkingBuoyTimeSlice(MarkingBuoyTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
