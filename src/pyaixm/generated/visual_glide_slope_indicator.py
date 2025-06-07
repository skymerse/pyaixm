from dataclasses import dataclass

from pyaixm.generated.visual_glide_slope_indicator_type import (
    VisualGlideSlopeIndicatorType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class VisualGlideSlopeIndicator(VisualGlideSlopeIndicatorType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
