from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.missed_approach_leg_time_slice import (
    MissedApproachLegTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class MissedApproachLegTimeSlicePropertyType:
    missed_approach_leg_time_slice: Optional[MissedApproachLegTimeSlice] = (
        field(
            default=None,
            metadata={
                "name": "MissedApproachLegTimeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "required": True,
            },
        )
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
