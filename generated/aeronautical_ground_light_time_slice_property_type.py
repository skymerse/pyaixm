from dataclasses import dataclass, field
from typing import Optional

from generated.aeronautical_ground_light_time_slice import (
    AeronauticalGroundLightTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AeronauticalGroundLightTimeSlicePropertyType:
    aeronautical_ground_light_time_slice: Optional[
        AeronauticalGroundLightTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "AeronauticalGroundLightTimeSlice",
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
