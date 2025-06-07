from dataclasses import dataclass, field
from typing import Optional

from generated.air_traffic_control_service_time_slice import (
    AirTrafficControlServiceTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirTrafficControlServiceTimeSlicePropertyType:
    air_traffic_control_service_time_slice: Optional[
        AirTrafficControlServiceTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "AirTrafficControlServiceTimeSlice",
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
