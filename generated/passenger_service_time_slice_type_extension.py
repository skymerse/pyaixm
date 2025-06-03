from dataclasses import dataclass, field
from typing import Optional

from generated.airport_ground_service_extension import (
    AirportGroundServiceExtension,
)
from generated.passenger_service_extension import PassengerServiceExtension
from generated.service_extension_1 import ServiceExtension1
from generated.service_extension_2 import ServiceExtension2

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PassengerServiceTimeSliceTypeExtension:
    class Meta:
        global_type = False

    passenger_service_extension: Optional[PassengerServiceExtension] = field(
        default=None,
        metadata={
            "name": "PassengerServiceExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    airport_ground_service_extension: Optional[
        AirportGroundServiceExtension
    ] = field(
        default=None,
        metadata={
            "name": "AirportGroundServiceExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    service_extension: Optional[ServiceExtension2] = field(
        default=None,
        metadata={
            "name": "ServiceExtension",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    aixm_aero_schema_5_1_event_service_extension: Optional[
        ServiceExtension1
    ] = field(
        default=None,
        metadata={
            "name": "ServiceExtension",
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
