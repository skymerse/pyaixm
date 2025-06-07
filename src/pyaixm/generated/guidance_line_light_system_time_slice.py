from dataclasses import dataclass

from pyaixm.generated.guidance_line_light_system_time_slice_type import (
    GuidanceLineLightSystemTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GuidanceLineLightSystemTimeSlice(GuidanceLineLightSystemTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
