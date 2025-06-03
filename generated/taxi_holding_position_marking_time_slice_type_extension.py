from dataclasses import dataclass, field
from typing import Optional

from generated.marking_extension import MarkingExtension
from generated.taxi_holding_position_marking_extension import (
    TaxiHoldingPositionMarkingExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TaxiHoldingPositionMarkingTimeSliceTypeExtension:
    class Meta:
        global_type = False

    taxi_holding_position_marking_extension: Optional[
        TaxiHoldingPositionMarkingExtension
    ] = field(
        default=None,
        metadata={
            "name": "TaxiHoldingPositionMarkingExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    marking_extension: Optional[MarkingExtension] = field(
        default=None,
        metadata={
            "name": "MarkingExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
