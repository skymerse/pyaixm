from dataclasses import dataclass

from generated.airport_heliport_availability_extension_type import (
    AirportHeliportAvailabilityExtensionType,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class AirportHeliportAvailabilityExtension(
    AirportHeliportAvailabilityExtensionType
):
    class Meta:
        namespace = "urn:us.gov.dot.faa.aim.fns"
