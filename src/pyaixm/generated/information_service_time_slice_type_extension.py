from dataclasses import dataclass, field
from typing import Optional

from generated.information_service_extension import InformationServiceExtension
from generated.service_extension_1 import ServiceExtension1
from generated.service_extension_2 import ServiceExtension2

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class InformationServiceTimeSliceTypeExtension:
    class Meta:
        global_type = False

    information_service_extension: Optional[InformationServiceExtension] = (
        field(
            default=None,
            metadata={
                "name": "InformationServiceExtension",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1/event",
            },
        )
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
