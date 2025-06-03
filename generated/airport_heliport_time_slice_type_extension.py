from dataclasses import dataclass, field
from typing import Optional

from generated.airport_heliport_extension_1 import AirportHeliportExtension1
from generated.airport_heliport_extension_2 import AirportHeliportExtension2

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportHeliportTimeSliceTypeExtension:
    class Meta:
        global_type = False

    airport_heliport_extension: Optional[AirportHeliportExtension2] = field(
        default=None,
        metadata={
            "name": "AirportHeliportExtension",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    aixm_aero_schema_5_1_event_airport_heliport_extension: Optional[
        AirportHeliportExtension1
    ] = field(
        default=None,
        metadata={
            "name": "AirportHeliportExtension",
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
