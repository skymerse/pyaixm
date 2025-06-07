from dataclasses import dataclass

from pyaixm.generated.passenger_service_type import PassengerServiceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PassengerService(PassengerServiceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
