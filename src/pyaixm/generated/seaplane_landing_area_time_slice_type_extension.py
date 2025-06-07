from dataclasses import dataclass, field
from typing import Optional

from generated.seaplane_landing_area_extension import (
    SeaplaneLandingAreaExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SeaplaneLandingAreaTimeSliceTypeExtension:
    class Meta:
        global_type = False

    seaplane_landing_area_extension: Optional[SeaplaneLandingAreaExtension] = (
        field(
            default=None,
            metadata={
                "name": "SeaplaneLandingAreaExtension",
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
