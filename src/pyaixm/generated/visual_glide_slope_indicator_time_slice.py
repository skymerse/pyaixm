from dataclasses import dataclass

from generated.visual_glide_slope_indicator_time_slice_type import (
    VisualGlideSlopeIndicatorTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class VisualGlideSlopeIndicatorTimeSlice(
    VisualGlideSlopeIndicatorTimeSliceType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
