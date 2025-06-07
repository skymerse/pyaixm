from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.passenger_loading_bridge_extension import (
    PassengerLoadingBridgeExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PassengerLoadingBridgeTimeSliceTypeExtension:
    class Meta:
        global_type = False

    passenger_loading_bridge_extension: Optional[
        PassengerLoadingBridgeExtension
    ] = field(
        default=None,
        metadata={
            "name": "PassengerLoadingBridgeExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
