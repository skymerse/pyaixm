from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.airport_heliport_availability_extension import (
    AirportHeliportAvailabilityExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportHeliportAvailabilityTypeExtension:
    class Meta:
        global_type = False

    airport_heliport_availability_extension: Optional[
        AirportHeliportAvailabilityExtension
    ] = field(
        default=None,
        metadata={
            "name": "AirportHeliportAvailabilityExtension",
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
