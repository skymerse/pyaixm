from dataclasses import dataclass

from pyaixm.generated.airport_heliport_extension_type_2 import (
    AirportHeliportExtensionType2,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class AirportHeliportExtension2(AirportHeliportExtensionType2):
    class Meta:
        name = "AirportHeliportExtension"
        namespace = "urn:us.gov.dot.faa.aim.fns"
