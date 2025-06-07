from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.ground_traffic_control_service_time_slice import (
    GroundTrafficControlServiceTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GroundTrafficControlServiceTimeSlicePropertyType:
    ground_traffic_control_service_time_slice: Optional[
        GroundTrafficControlServiceTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "GroundTrafficControlServiceTimeSlice",
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
