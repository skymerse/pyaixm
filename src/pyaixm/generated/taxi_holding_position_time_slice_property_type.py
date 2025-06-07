from dataclasses import dataclass, field
from typing import Optional

from generated.taxi_holding_position_time_slice import (
    TaxiHoldingPositionTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiHoldingPositionTimeSlicePropertyType:
    taxi_holding_position_time_slice: Optional[
        TaxiHoldingPositionTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "TaxiHoldingPositionTimeSlice",
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
