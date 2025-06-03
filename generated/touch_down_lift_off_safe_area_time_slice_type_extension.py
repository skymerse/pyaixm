from dataclasses import dataclass, field
from typing import Optional

from generated.airport_heliport_protection_area_extension import (
    AirportHeliportProtectionAreaExtension,
)
from generated.touch_down_lift_off_safe_area_extension import (
    TouchDownLiftOffSafeAreaExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TouchDownLiftOffSafeAreaTimeSliceTypeExtension:
    class Meta:
        global_type = False

    touch_down_lift_off_safe_area_extension: Optional[
        TouchDownLiftOffSafeAreaExtension
    ] = field(
        default=None,
        metadata={
            "name": "TouchDownLiftOffSafeAreaExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    airport_heliport_protection_area_extension: Optional[
        AirportHeliportProtectionAreaExtension
    ] = field(
        default=None,
        metadata={
            "name": "AirportHeliportProtectionAreaExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
