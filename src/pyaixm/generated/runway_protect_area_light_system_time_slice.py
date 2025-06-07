from dataclasses import dataclass

from pyaixm.generated.runway_protect_area_light_system_time_slice_type import (
    RunwayProtectAreaLightSystemTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayProtectAreaLightSystemTimeSlice(
    RunwayProtectAreaLightSystemTimeSliceType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
