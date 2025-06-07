from dataclasses import dataclass

from generated.aircraft_characteristic_type import AircraftCharacteristicType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AircraftCharacteristic(AircraftCharacteristicType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
