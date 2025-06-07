from dataclasses import dataclass

from generated.terminal_arrival_area_time_slice_type import (
    TerminalArrivalAreaTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TerminalArrivalAreaTimeSlice(TerminalArrivalAreaTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
