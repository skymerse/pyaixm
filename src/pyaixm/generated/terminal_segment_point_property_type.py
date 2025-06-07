from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.terminal_segment_point import TerminalSegmentPoint

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TerminalSegmentPointPropertyType(AbstractAixmpropertyType):
    terminal_segment_point: Optional[TerminalSegmentPoint] = field(
        default=None,
        metadata={
            "name": "TerminalSegmentPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
