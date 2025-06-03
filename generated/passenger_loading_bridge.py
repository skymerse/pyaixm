from dataclasses import dataclass

from generated.passenger_loading_bridge_type import PassengerLoadingBridgeType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PassengerLoadingBridge(PassengerLoadingBridgeType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
