from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.wind_direction_indicator_time_slice import (
    WindDirectionIndicatorTimeSlice,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class WindDirectionIndicatorTimeSlicePropertyType:
    wind_direction_indicator_time_slice: Optional[
        WindDirectionIndicatorTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "WindDirectionIndicatorTimeSlice",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
            "required": True,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
