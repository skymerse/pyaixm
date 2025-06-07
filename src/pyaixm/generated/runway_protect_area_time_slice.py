from dataclasses import dataclass

from pyaixm.generated.runway_protect_area_time_slice_type import (
    RunwayProtectAreaTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayProtectAreaTimeSlice(RunwayProtectAreaTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
