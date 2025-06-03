from dataclasses import dataclass

from generated.apron_area_availability_extension_type import (
    ApronAreaAvailabilityExtensionType,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class ApronAreaAvailabilityExtension(ApronAreaAvailabilityExtensionType):
    class Meta:
        namespace = "urn:us.gov.dot.faa.aim.fns"
