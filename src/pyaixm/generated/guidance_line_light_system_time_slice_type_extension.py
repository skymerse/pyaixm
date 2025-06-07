from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.ground_light_system_extension import (
    GroundLightSystemExtension,
)
from pyaixm.generated.guidance_line_light_system_extension import (
    GuidanceLineLightSystemExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GuidanceLineLightSystemTimeSliceTypeExtension:
    class Meta:
        global_type = False

    guidance_line_light_system_extension: Optional[
        GuidanceLineLightSystemExtension
    ] = field(
        default=None,
        metadata={
            "name": "GuidanceLineLightSystemExtension",
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
