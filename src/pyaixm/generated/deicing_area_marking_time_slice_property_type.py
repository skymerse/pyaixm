from dataclasses import dataclass, field
from typing import Optional

from generated.deicing_area_marking_time_slice import (
    DeicingAreaMarkingTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DeicingAreaMarkingTimeSlicePropertyType:
    deicing_area_marking_time_slice: Optional[DeicingAreaMarkingTimeSlice] = (
        field(
            default=None,
            metadata={
                "name": "DeicingAreaMarkingTimeSlice",
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
