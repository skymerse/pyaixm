from dataclasses import dataclass, field
from typing import Optional

from generated.flight_restriction_extension import FlightRestrictionExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FlightRestrictionTimeSliceTypeExtension:
    class Meta:
        global_type = False

    flight_restriction_extension: Optional[FlightRestrictionExtension] = field(
        default=None,
        metadata={
            "name": "FlightRestrictionExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
