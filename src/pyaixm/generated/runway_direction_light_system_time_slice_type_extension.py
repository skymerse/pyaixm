from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.ground_light_system_extension import (
    GroundLightSystemExtension,
)
from pyaixm.generated.runway_direction_light_system_extension_1 import (
    RunwayDirectionLightSystemExtension1,
)
from pyaixm.generated.runway_direction_light_system_extension_2 import (
    RunwayDirectionLightSystemExtension2,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayDirectionLightSystemTimeSliceTypeExtension:
    class Meta:
        global_type = False

    runway_direction_light_system_extension: Optional[
        RunwayDirectionLightSystemExtension2
    ] = field(
        default=None,
        metadata={
            "name": "RunwayDirectionLightSystemExtension",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    aixm_aero_schema_5_1_event_runway_direction_light_system_extension: Optional[
        RunwayDirectionLightSystemExtension1
    ] = field(
        default=None,
        metadata={
            "name": "RunwayDirectionLightSystemExtension",
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
