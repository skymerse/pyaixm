from dataclasses import dataclass

from generated.runway_direction_light_system_time_slice_type import (
    RunwayDirectionLightSystemTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayDirectionLightSystemTimeSlice(
    RunwayDirectionLightSystemTimeSliceType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
