from dataclasses import dataclass

from pyaixm.generated.passenger_service_extension_type import (
    PassengerServiceExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class PassengerServiceExtension(PassengerServiceExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
