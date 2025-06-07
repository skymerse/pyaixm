from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.route_dmetime_slice import RouteDmetimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RouteDmetimeSlicePropertyType:
    class Meta:
        name = "RouteDMETimeSlicePropertyType"

    route_dmetime_slice: Optional[RouteDmetimeSlice] = field(
        default=None,
        metadata={
            "name": "RouteDMETimeSlice",
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
