from dataclasses import dataclass

from generated.guidance_line_time_slice_type import GuidanceLineTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GuidanceLineTimeSlice(GuidanceLineTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
