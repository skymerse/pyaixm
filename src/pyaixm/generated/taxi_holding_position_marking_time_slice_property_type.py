from dataclasses import dataclass, field
from typing import Optional

from generated.taxi_holding_position_marking_time_slice import (
    TaxiHoldingPositionMarkingTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiHoldingPositionMarkingTimeSlicePropertyType:
    taxi_holding_position_marking_time_slice: Optional[
        TaxiHoldingPositionMarkingTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "TaxiHoldingPositionMarkingTimeSlice",
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
