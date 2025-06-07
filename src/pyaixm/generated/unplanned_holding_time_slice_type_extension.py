from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.unplanned_holding_extension import (
    UnplannedHoldingExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class UnplannedHoldingTimeSliceTypeExtension:
    class Meta:
        global_type = False

    unplanned_holding_extension: Optional[UnplannedHoldingExtension] = field(
        default=None,
        metadata={
            "name": "UnplannedHoldingExtension",
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
