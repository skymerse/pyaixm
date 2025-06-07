from dataclasses import dataclass

from pyaixm.generated.runway_direction_time_slice_type import (
    RunwayDirectionTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayDirectionTimeSlice(RunwayDirectionTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
