from dataclasses import dataclass

from pyaixm.generated.runway_time_slice_type import RunwayTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayTimeSlice(RunwayTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
