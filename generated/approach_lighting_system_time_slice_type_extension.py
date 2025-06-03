from dataclasses import dataclass, field
from typing import Optional

from generated.approach_lighting_system_extension import (
    ApproachLightingSystemExtension,
)
from generated.ground_light_system_extension import GroundLightSystemExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApproachLightingSystemTimeSliceTypeExtension:
    class Meta:
        global_type = False

    approach_lighting_system_extension: Optional[
        ApproachLightingSystemExtension
    ] = field(
        default=None,
        metadata={
            "name": "ApproachLightingSystemExtension",
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
