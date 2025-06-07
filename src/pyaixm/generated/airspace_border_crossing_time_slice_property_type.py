from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.airspace_border_crossing_time_slice import (
    AirspaceBorderCrossingTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirspaceBorderCrossingTimeSlicePropertyType:
    airspace_border_crossing_time_slice: Optional[
        AirspaceBorderCrossingTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "AirspaceBorderCrossingTimeSlice",
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
