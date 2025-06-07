from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.air_traffic_management_service_time_slice import (
    AirTrafficManagementServiceTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirTrafficManagementServiceTimeSlicePropertyType:
    air_traffic_management_service_time_slice: Optional[
        AirTrafficManagementServiceTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "AirTrafficManagementServiceTimeSlice",
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
