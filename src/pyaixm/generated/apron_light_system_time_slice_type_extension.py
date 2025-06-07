from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.apron_light_system_extension import (
    ApronLightSystemExtension,
)
from pyaixm.generated.ground_light_system_extension import (
    GroundLightSystemExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApronLightSystemTimeSliceTypeExtension:
    class Meta:
        global_type = False

    apron_light_system_extension: Optional[ApronLightSystemExtension] = field(
        default=None,
        metadata={
            "name": "ApronLightSystemExtension",
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
