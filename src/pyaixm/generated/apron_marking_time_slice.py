from dataclasses import dataclass

from generated.apron_marking_time_slice_type import ApronMarkingTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApronMarkingTimeSlice(ApronMarkingTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
