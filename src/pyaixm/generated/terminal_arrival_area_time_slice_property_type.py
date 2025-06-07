from dataclasses import dataclass, field
from typing import Optional

from generated.terminal_arrival_area_time_slice import (
    TerminalArrivalAreaTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TerminalArrivalAreaTimeSlicePropertyType:
    terminal_arrival_area_time_slice: Optional[
        TerminalArrivalAreaTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "TerminalArrivalAreaTimeSlice",
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
