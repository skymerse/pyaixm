from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.holding_pattern_time_slice import HoldingPatternTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class HoldingPatternTimeSlicePropertyType:
    holding_pattern_time_slice: Optional[HoldingPatternTimeSlice] = field(
        default=None,
        metadata={
            "name": "HoldingPatternTimeSlice",
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
