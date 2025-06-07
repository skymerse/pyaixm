from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.route_dmeextension import RouteDmeextension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RouteDmetimeSliceTypeExtension:
    class Meta:
        global_type = False

    route_dmeextension: Optional[RouteDmeextension] = field(
        default=None,
        metadata={
            "name": "RouteDMEExtension",
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
