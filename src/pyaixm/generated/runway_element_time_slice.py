from dataclasses import dataclass

from pyaixm.generated.runway_element_time_slice_type import (
    RunwayElementTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayElementTimeSlice(RunwayElementTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
