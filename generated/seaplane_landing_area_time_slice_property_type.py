from dataclasses import dataclass, field
from typing import Optional

from generated.seaplane_landing_area_time_slice import (
    SeaplaneLandingAreaTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SeaplaneLandingAreaTimeSlicePropertyType:
    seaplane_landing_area_time_slice: Optional[
        SeaplaneLandingAreaTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "SeaplaneLandingAreaTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
