from dataclasses import dataclass, field
from typing import Optional

from generated.runway_time_slice import RunwayTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayTimeSlicePropertyType:
    runway_time_slice: Optional[RunwayTimeSlice] = field(
        default=None,
        metadata={
            "name": "RunwayTimeSlice",
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
