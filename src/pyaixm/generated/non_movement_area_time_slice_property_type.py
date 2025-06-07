from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.non_movement_area_time_slice import (
    NonMovementAreaTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NonMovementAreaTimeSlicePropertyType:
    non_movement_area_time_slice: Optional[NonMovementAreaTimeSlice] = field(
        default=None,
        metadata={
            "name": "NonMovementAreaTimeSlice",
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
