from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_traffic_separation_service_type import (
    AbstractTrafficSeparationServiceType,
)
from generated.air_traffic_control_service_time_slice_property_type import (
    AirTrafficControlServiceTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirTrafficControlServiceType(AbstractTrafficSeparationServiceType):
    time_slice: Iterable[AirTrafficControlServiceTimeSlicePropertyType] = (
        field(
            default_factory=list,
            metadata={
                "name": "timeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "min_occurs": 1,
            },
        )
    )
