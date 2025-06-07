from dataclasses import dataclass, field
from typing import Optional

from generated.airport_heliport_protection_area_extension import (
    AirportHeliportProtectionAreaExtension,
)
from generated.runway_protect_area_extension import RunwayProtectAreaExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayProtectAreaTimeSliceTypeExtension:
    class Meta:
        global_type = False

    runway_protect_area_extension: Optional[RunwayProtectAreaExtension] = (
        field(
            default=None,
            metadata={
                "name": "RunwayProtectAreaExtension",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1/event",
            },
        )
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
