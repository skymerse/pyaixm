from dataclasses import dataclass

from generated.aircraft_characteristic_extension_type import (
    AircraftCharacteristicExtensionType,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class AircraftCharacteristicExtension(AircraftCharacteristicExtensionType):
    class Meta:
        namespace = "urn:us.gov.dot.faa.aim.fns"
