from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.route_time_slice import RouteTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RouteTimeSlicePropertyType:
    route_time_slice: Optional[RouteTimeSlice] = field(
        default=None,
        metadata={
            "name": "RouteTimeSlice",
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
