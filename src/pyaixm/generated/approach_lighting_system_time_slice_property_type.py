from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.approach_lighting_system_time_slice import (
    ApproachLightingSystemTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApproachLightingSystemTimeSlicePropertyType:
    approach_lighting_system_time_slice: Optional[
        ApproachLightingSystemTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "ApproachLightingSystemTimeSlice",
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
