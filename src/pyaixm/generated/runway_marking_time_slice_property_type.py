from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.runway_marking_time_slice import RunwayMarkingTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayMarkingTimeSlicePropertyType:
    runway_marking_time_slice: Optional[RunwayMarkingTimeSlice] = field(
        default=None,
        metadata={
            "name": "RunwayMarkingTimeSlice",
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
