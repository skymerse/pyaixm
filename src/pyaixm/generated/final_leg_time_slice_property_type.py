from dataclasses import dataclass, field
from typing import Optional

from generated.final_leg_time_slice import FinalLegTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FinalLegTimeSlicePropertyType:
    final_leg_time_slice: Optional[FinalLegTimeSlice] = field(
        default=None,
        metadata={
            "name": "FinalLegTimeSlice",
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
