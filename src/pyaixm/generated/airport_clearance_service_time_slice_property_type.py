from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.airport_clearance_service_time_slice import (
    AirportClearanceServiceTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportClearanceServiceTimeSlicePropertyType:
    airport_clearance_service_time_slice: Optional[
        AirportClearanceServiceTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "AirportClearanceServiceTimeSlice",
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
