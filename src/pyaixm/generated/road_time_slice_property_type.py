from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.road_time_slice import RoadTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RoadTimeSlicePropertyType:
    road_time_slice: Optional[RoadTimeSlice] = field(
        default=None,
        metadata={
            "name": "RoadTimeSlice",
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
