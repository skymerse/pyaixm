from dataclasses import dataclass, field
from typing import Optional

from generated.circling_area_time_slice import CirclingAreaTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CirclingAreaTimeSlicePropertyType:
    circling_area_time_slice: Optional[CirclingAreaTimeSlice] = field(
        default=None,
        metadata={
            "name": "CirclingAreaTimeSlice",
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
