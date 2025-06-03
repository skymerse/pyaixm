from dataclasses import dataclass, field
from typing import Optional

from generated.ground_light_system_extension import GroundLightSystemExtension
from generated.runway_protect_area_light_system_extension import (
    RunwayProtectAreaLightSystemExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayProtectAreaLightSystemTimeSliceTypeExtension:
    class Meta:
        global_type = False

    runway_protect_area_light_system_extension: Optional[
        RunwayProtectAreaLightSystemExtension
    ] = field(
        default=None,
        metadata={
            "name": "RunwayProtectAreaLightSystemExtension",
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
