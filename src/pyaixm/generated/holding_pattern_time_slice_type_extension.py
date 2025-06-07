from dataclasses import dataclass, field
from typing import Optional

from generated.holding_pattern_extension import HoldingPatternExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class HoldingPatternTimeSliceTypeExtension:
    class Meta:
        global_type = False

    holding_pattern_extension: Optional[HoldingPatternExtension] = field(
        default=None,
        metadata={
            "name": "HoldingPatternExtension",
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
