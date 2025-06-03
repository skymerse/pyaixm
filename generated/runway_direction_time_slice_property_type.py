from dataclasses import dataclass, field
from typing import Optional

from generated.runway_direction_time_slice import RunwayDirectionTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayDirectionTimeSlicePropertyType:
    runway_direction_time_slice: Optional[RunwayDirectionTimeSlice] = field(
        default=None,
        metadata={
            "name": "RunwayDirectionTimeSlice",
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
