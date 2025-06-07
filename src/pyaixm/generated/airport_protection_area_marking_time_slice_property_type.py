from dataclasses import dataclass, field
from typing import Optional

from generated.airport_protection_area_marking_time_slice import (
    AirportProtectionAreaMarkingTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportProtectionAreaMarkingTimeSlicePropertyType:
    airport_protection_area_marking_time_slice: Optional[
        AirportProtectionAreaMarkingTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "AirportProtectionAreaMarkingTimeSlice",
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
