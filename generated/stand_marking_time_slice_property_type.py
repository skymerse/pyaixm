from dataclasses import dataclass, field
from typing import Optional

from generated.stand_marking_time_slice import StandMarkingTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandMarkingTimeSlicePropertyType:
    stand_marking_time_slice: Optional[StandMarkingTimeSlice] = field(
        default=None,
        metadata={
            "name": "StandMarkingTimeSlice",
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
