from dataclasses import dataclass, field
from typing import Optional

from generated.ground_light_system_extension import GroundLightSystemExtension
from generated.visual_glide_slope_indicator_extension import (
    VisualGlideSlopeIndicatorExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class VisualGlideSlopeIndicatorTimeSliceTypeExtension:
    class Meta:
        global_type = False

    visual_glide_slope_indicator_extension: Optional[
        VisualGlideSlopeIndicatorExtension
    ] = field(
        default=None,
        metadata={
            "name": "VisualGlideSlopeIndicatorExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    ground_light_system_extension: Optional[GroundLightSystemExtension] = (
        field(
            default=None,
            metadata={
                "name": "GroundLightSystemExtension",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1/event",
            },
        )
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
