from dataclasses import dataclass, field
from typing import Optional

from generated.ground_light_system_extension import GroundLightSystemExtension
from generated.touch_down_lift_off_light_system_extension import (
    TouchDownLiftOffLightSystemExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TouchDownLiftOffLightSystemTimeSliceTypeExtension:
    class Meta:
        global_type = False

    touch_down_lift_off_light_system_extension: Optional[
        TouchDownLiftOffLightSystemExtension
    ] = field(
        default=None,
        metadata={
            "name": "TouchDownLiftOffLightSystemExtension",
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
