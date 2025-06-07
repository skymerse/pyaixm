from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_airport_ground_service_type import (
    AbstractAirportGroundServiceType,
)
from generated.airport_supplies_service_time_slice_property_type import (
    AirportSuppliesServiceTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportSuppliesServiceType(AbstractAirportGroundServiceType):
    time_slice: Iterable[AirportSuppliesServiceTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
