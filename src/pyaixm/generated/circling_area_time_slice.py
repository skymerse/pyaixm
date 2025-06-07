from dataclasses import dataclass

from generated.circling_area_time_slice_type import CirclingAreaTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CirclingAreaTimeSlice(CirclingAreaTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
