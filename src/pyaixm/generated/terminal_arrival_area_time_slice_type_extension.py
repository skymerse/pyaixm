from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.terminal_arrival_area_extension import (
    TerminalArrivalAreaExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TerminalArrivalAreaTimeSliceTypeExtension:
    class Meta:
        global_type = False

    terminal_arrival_area_extension: Optional[TerminalArrivalAreaExtension] = (
        field(
            default=None,
            metadata={
                "name": "TerminalArrivalAreaExtension",
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
