from dataclasses import dataclass, field
from typing import Optional

from generated.unplanned_holding_time_slice import UnplannedHoldingTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class UnplannedHoldingTimeSlicePropertyType:
    unplanned_holding_time_slice: Optional[UnplannedHoldingTimeSlice] = field(
        default=None,
        metadata={
            "name": "UnplannedHoldingTimeSlice",
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
