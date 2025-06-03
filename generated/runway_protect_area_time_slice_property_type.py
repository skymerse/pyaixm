from dataclasses import dataclass, field
from typing import Optional

from generated.runway_protect_area_time_slice import RunwayProtectAreaTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayProtectAreaTimeSlicePropertyType:
    runway_protect_area_time_slice: Optional[RunwayProtectAreaTimeSlice] = (
        field(
            default=None,
            metadata={
                "name": "RunwayProtectAreaTimeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "required": True,
            },
        )
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
