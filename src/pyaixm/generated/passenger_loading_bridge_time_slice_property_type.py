from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.passenger_loading_bridge_time_slice import (
    PassengerLoadingBridgeTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PassengerLoadingBridgeTimeSlicePropertyType:
    passenger_loading_bridge_time_slice: Optional[
        PassengerLoadingBridgeTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "PassengerLoadingBridgeTimeSlice",
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
