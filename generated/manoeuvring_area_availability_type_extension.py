from dataclasses import dataclass, field
from typing import Optional

from generated.manoeuvring_area_availability_extension import (
    ManoeuvringAreaAvailabilityExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ManoeuvringAreaAvailabilityTypeExtension:
    class Meta:
        global_type = False

    manoeuvring_area_availability_extension: Optional[
        ManoeuvringAreaAvailabilityExtension
    ] = field(
        default=None,
        metadata={
            "name": "ManoeuvringAreaAvailabilityExtension",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
