from dataclasses import dataclass, field
from typing import Optional

from generated.departure_leg_time_slice import DepartureLegTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DepartureLegTimeSlicePropertyType:
    departure_leg_time_slice: Optional[DepartureLegTimeSlice] = field(
        default=None,
        metadata={
            "name": "DepartureLegTimeSlice",
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
