from dataclasses import dataclass

from generated.manoeuvring_area_availability_extension_type import (
    ManoeuvringAreaAvailabilityExtensionType,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class ManoeuvringAreaAvailabilityExtension(
    ManoeuvringAreaAvailabilityExtensionType
):
    class Meta:
        namespace = "urn:us.gov.dot.faa.aim.fns"
