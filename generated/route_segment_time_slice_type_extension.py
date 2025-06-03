from dataclasses import dataclass, field
from typing import Optional

from generated.route_segment_extension_1 import RouteSegmentExtension1
from generated.route_segment_extension_2 import RouteSegmentExtension2

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RouteSegmentTimeSliceTypeExtension:
    class Meta:
        global_type = False

    route_segment_extension: Optional[RouteSegmentExtension2] = field(
        default=None,
        metadata={
            "name": "RouteSegmentExtension",
            "type": "Element",
            "namespace": "urn:us.gov.dot.faa.aim.fns",
        },
    )
    aixm_aero_schema_5_1_event_route_segment_extension: Optional[
        RouteSegmentExtension1
    ] = field(
        default=None,
        metadata={
            "name": "RouteSegmentExtension",
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
