from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_service_type import AbstractServiceType
from generated.air_traffic_management_service_time_slice_property_type import (
    AirTrafficManagementServiceTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirTrafficManagementServiceType(AbstractServiceType):
    time_slice: Iterable[AirTrafficManagementServiceTimeSlicePropertyType] = (
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
