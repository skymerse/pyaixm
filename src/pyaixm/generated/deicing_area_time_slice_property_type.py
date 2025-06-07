from dataclasses import dataclass, field
from typing import Optional

from generated.deicing_area_time_slice import DeicingAreaTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DeicingAreaTimeSlicePropertyType:
    deicing_area_time_slice: Optional[DeicingAreaTimeSlice] = field(
        default=None,
        metadata={
            "name": "DeicingAreaTimeSlice",
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
