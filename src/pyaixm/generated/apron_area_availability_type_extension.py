from dataclasses import dataclass, field
from typing import Optional

from generated.apron_area_availability_extension import (
    ApronAreaAvailabilityExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApronAreaAvailabilityTypeExtension:
    class Meta:
        global_type = False

    apron_area_availability_extension: Optional[
        ApronAreaAvailabilityExtension
    ] = field(
        default=None,
        metadata={
            "name": "ApronAreaAvailabilityExtension",
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
