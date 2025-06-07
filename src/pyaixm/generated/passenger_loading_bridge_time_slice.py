from dataclasses import dataclass

from generated.passenger_loading_bridge_time_slice_type import (
    PassengerLoadingBridgeTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PassengerLoadingBridgeTimeSlice(PassengerLoadingBridgeTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
