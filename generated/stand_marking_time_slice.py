from dataclasses import dataclass

from generated.stand_marking_time_slice_type import StandMarkingTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandMarkingTimeSlice(StandMarkingTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
