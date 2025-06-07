from dataclasses import dataclass, field
from typing import Optional

from generated.route_segment_time_slice import RouteSegmentTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RouteSegmentTimeSlicePropertyType:
    route_segment_time_slice: Optional[RouteSegmentTimeSlice] = field(
        default=None,
        metadata={
            "name": "RouteSegmentTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
