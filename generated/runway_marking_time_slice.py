from dataclasses import dataclass

from generated.runway_marking_time_slice_type import RunwayMarkingTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayMarkingTimeSlice(RunwayMarkingTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
