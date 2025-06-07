from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.airport_ground_service_extension import (
    AirportGroundServiceExtension,
)
from pyaixm.generated.airport_supplies_service_extension import (
    AirportSuppliesServiceExtension,
)
from pyaixm.generated.service_extension_1 import ServiceExtension1
from pyaixm.generated.service_extension_2 import ServiceExtension2

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportSuppliesServiceTimeSliceTypeExtension:
    class Meta:
        global_type = False

    airport_supplies_service_extension: Optional[
        AirportSuppliesServiceExtension
    ] = field(
        default=None,
        metadata={
            "name": "AirportSuppliesServiceExtension",
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
