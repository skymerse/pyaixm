from dataclasses import dataclass, field
from typing import Optional

from generated.change_over_point_time_slice import ChangeOverPointTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ChangeOverPointTimeSlicePropertyType:
    change_over_point_time_slice: Optional[ChangeOverPointTimeSlice] = field(
        default=None,
        metadata={
            "name": "ChangeOverPointTimeSlice",
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
