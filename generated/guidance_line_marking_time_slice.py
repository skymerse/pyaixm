from dataclasses import dataclass

from generated.guidance_line_marking_time_slice_type import (
    GuidanceLineMarkingTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GuidanceLineMarkingTimeSlice(GuidanceLineMarkingTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
