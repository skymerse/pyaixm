from dataclasses import dataclass

from generated.terminal_arrival_area_type import TerminalArrivalAreaType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TerminalArrivalArea(TerminalArrivalAreaType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
