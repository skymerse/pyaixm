from dataclasses import dataclass

from pyaixm.generated.flight_characteristic_type import (
    FlightCharacteristicType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FlightCharacteristic(FlightCharacteristicType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
