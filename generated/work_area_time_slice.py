from dataclasses import dataclass

from generated.work_area_time_slice_type import WorkAreaTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class WorkAreaTimeSlice(WorkAreaTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
