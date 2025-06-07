from dataclasses import dataclass, field
from typing import Optional

from generated.passenger_service_time_slice import PassengerServiceTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PassengerServiceTimeSlicePropertyType:
    passenger_service_time_slice: Optional[PassengerServiceTimeSlice] = field(
        default=None,
        metadata={
            "name": "PassengerServiceTimeSlice",
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
