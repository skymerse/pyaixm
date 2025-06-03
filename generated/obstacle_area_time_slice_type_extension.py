from dataclasses import dataclass, field
from typing import Optional

from generated.obstacle_area_extension import ObstacleAreaExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ObstacleAreaTimeSliceTypeExtension:
    class Meta:
        global_type = False

    obstacle_area_extension: Optional[ObstacleAreaExtension] = field(
        default=None,
        metadata={
            "name": "ObstacleAreaExtension",
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
