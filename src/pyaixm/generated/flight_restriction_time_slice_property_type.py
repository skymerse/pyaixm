from dataclasses import dataclass, field
from typing import Optional

from generated.flight_restriction_time_slice import FlightRestrictionTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FlightRestrictionTimeSlicePropertyType:
    flight_restriction_time_slice: Optional[FlightRestrictionTimeSlice] = (
        field(
            default=None,
            metadata={
                "name": "FlightRestrictionTimeSlice",
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
