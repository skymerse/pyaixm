from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.aircraft_stand_time_slice import AircraftStandTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AircraftStandTimeSlicePropertyType:
    aircraft_stand_time_slice: Optional[AircraftStandTimeSlice] = field(
        default=None,
        metadata={
            "name": "AircraftStandTimeSlice",
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
