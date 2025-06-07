from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.precision_approach_radar_time_slice import (
    PrecisionApproachRadarTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PrecisionApproachRadarTimeSlicePropertyType:
    precision_approach_radar_time_slice: Optional[
        PrecisionApproachRadarTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "PrecisionApproachRadarTimeSlice",
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
