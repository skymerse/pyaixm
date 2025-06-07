from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.airport_hot_spot_time_slice import (
    AirportHotSpotTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportHotSpotTimeSlicePropertyType:
    airport_hot_spot_time_slice: Optional[AirportHotSpotTimeSlice] = field(
        default=None,
        metadata={
            "name": "AirportHotSpotTimeSlice",
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
