from dataclasses import dataclass, field
from typing import Optional

from generated.arrival_leg_time_slice import ArrivalLegTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ArrivalLegTimeSlicePropertyType:
    arrival_leg_time_slice: Optional[ArrivalLegTimeSlice] = field(
        default=None,
        metadata={
            "name": "ArrivalLegTimeSlice",
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
