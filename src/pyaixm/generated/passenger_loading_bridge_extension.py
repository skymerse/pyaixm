from dataclasses import dataclass

from pyaixm.generated.passenger_loading_bridge_extension_type import (
    PassengerLoadingBridgeExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class PassengerLoadingBridgeExtension(PassengerLoadingBridgeExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
