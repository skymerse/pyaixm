from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.taxi_holding_position_light_system_time_slice import (
    TaxiHoldingPositionLightSystemTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiHoldingPositionLightSystemTimeSlicePropertyType:
    taxi_holding_position_light_system_time_slice: Optional[
        TaxiHoldingPositionLightSystemTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "TaxiHoldingPositionLightSystemTimeSlice",
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
