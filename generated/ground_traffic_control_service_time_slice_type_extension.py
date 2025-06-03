from dataclasses import dataclass, field
from typing import Optional

from generated.ground_traffic_control_service_extension import (
    GroundTrafficControlServiceExtension,
)
from generated.service_extension_1 import ServiceExtension1
from generated.service_extension_2 import ServiceExtension2
from generated.traffic_separation_service_extension import (
    TrafficSeparationServiceExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GroundTrafficControlServiceTimeSliceTypeExtension:
    class Meta:
        global_type = False

    ground_traffic_control_service_extension: Optional[
        GroundTrafficControlServiceExtension
    ] = field(
        default=None,
        metadata={
            "name": "GroundTrafficControlServiceExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    traffic_separation_service_extension: Optional[
        TrafficSeparationServiceExtension
    ] = field(
        default=None,
        metadata={
            "name": "TrafficSeparationServiceExtension",
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
