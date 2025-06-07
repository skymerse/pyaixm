from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.intermediate_leg_time_slice import (
    IntermediateLegTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class IntermediateLegTimeSlicePropertyType:
    intermediate_leg_time_slice: Optional[IntermediateLegTimeSlice] = field(
        default=None,
        metadata={
            "name": "IntermediateLegTimeSlice",
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
