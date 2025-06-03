from dataclasses import dataclass, field
from typing import Optional

from generated.arresting_gear_time_slice import ArrestingGearTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ArrestingGearTimeSlicePropertyType:
    arresting_gear_time_slice: Optional[ArrestingGearTimeSlice] = field(
        default=None,
        metadata={
            "name": "ArrestingGearTimeSlice",
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
