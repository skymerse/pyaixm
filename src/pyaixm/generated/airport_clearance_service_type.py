from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_airport_ground_service_type import (
    AbstractAirportGroundServiceType,
)
from pyaixm.generated.airport_clearance_service_time_slice_property_type import (
    AirportClearanceServiceTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportClearanceServiceType(AbstractAirportGroundServiceType):
    time_slice: Iterable[AirportClearanceServiceTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
