from dataclasses import dataclass

from pyaixm.generated.visual_glide_slope_indicator_extension_type import (
    VisualGlideSlopeIndicatorExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class VisualGlideSlopeIndicatorExtension(
    VisualGlideSlopeIndicatorExtensionType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
