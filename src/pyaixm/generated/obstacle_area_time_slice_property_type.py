from dataclasses import dataclass, field
from typing import Optional

from generated.obstacle_area_time_slice import ObstacleAreaTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ObstacleAreaTimeSlicePropertyType:
    obstacle_area_time_slice: Optional[ObstacleAreaTimeSlice] = field(
        default=None,
        metadata={
            "name": "ObstacleAreaTimeSlice",
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
