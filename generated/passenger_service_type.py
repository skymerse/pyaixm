from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_airport_ground_service_type import (
    AbstractAirportGroundServiceType,
)
from generated.passenger_service_time_slice_property_type import (
    PassengerServiceTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PassengerServiceType(AbstractAirportGroundServiceType):
    time_slice: Iterable[PassengerServiceTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
