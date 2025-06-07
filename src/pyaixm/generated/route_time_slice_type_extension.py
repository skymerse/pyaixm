from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.route_extension import RouteExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RouteTimeSliceTypeExtension:
    class Meta:
        global_type = False

    route_extension: Optional[RouteExtension] = field(
        default=None,
        metadata={
            "name": "RouteExtension",
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
