from dataclasses import dataclass, field
from typing import Optional

from generated.aircraft_ground_service_time_slice import (
    AircraftGroundServiceTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AircraftGroundServiceTimeSlicePropertyType:
    aircraft_ground_service_time_slice: Optional[
        AircraftGroundServiceTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "AircraftGroundServiceTimeSlice",
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
