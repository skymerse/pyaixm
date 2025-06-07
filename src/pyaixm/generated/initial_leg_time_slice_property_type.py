from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.initial_leg_time_slice import InitialLegTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class InitialLegTimeSlicePropertyType:
    initial_leg_time_slice: Optional[InitialLegTimeSlice] = field(
        default=None,
        metadata={
            "name": "InitialLegTimeSlice",
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
