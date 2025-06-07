from dataclasses import dataclass

from generated.terminal_segment_point_type import TerminalSegmentPointType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TerminalSegmentPoint(TerminalSegmentPointType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
