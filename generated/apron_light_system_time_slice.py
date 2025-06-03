from dataclasses import dataclass

from generated.apron_light_system_time_slice_type import (
    ApronLightSystemTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApronLightSystemTimeSlice(ApronLightSystemTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
