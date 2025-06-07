from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.aerial_refuelling_point import AerialRefuellingPoint
from pyaixm.generated.en_route_segment_point import EnRouteSegmentPoint
from pyaixm.generated.terminal_segment_point import TerminalSegmentPoint

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SegmentPointPropertyType(AbstractAixmpropertyType):
    aerial_refuelling_point: Optional[AerialRefuellingPoint] = field(
        default=None,
        metadata={
            "name": "AerialRefuellingPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    en_route_segment_point: Optional[EnRouteSegmentPoint] = field(
        default=None,
        metadata={
            "name": "EnRouteSegmentPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    terminal_segment_point: Optional[TerminalSegmentPoint] = field(
        default=None,
        metadata={
            "name": "TerminalSegmentPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
