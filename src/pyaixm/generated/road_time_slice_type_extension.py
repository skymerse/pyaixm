from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.road_extension import RoadExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RoadTimeSliceTypeExtension:
    class Meta:
        global_type = False

    road_extension: Optional[RoadExtension] = field(
        default=None,
        metadata={
            "name": "RoadExtension",
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
