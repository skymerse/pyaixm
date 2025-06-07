from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.taxi_holding_position_extension import (
    TaxiHoldingPositionExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiHoldingPositionTimeSliceTypeExtension:
    class Meta:
        global_type = False

    taxi_holding_position_extension: Optional[TaxiHoldingPositionExtension] = (
        field(
            default=None,
            metadata={
                "name": "TaxiHoldingPositionExtension",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1/event",
            },
        )
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
