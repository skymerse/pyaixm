from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.en_route_segment_point import EnRouteSegmentPoint

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class EnRouteSegmentPointPropertyType(AbstractAixmpropertyType):
    en_route_segment_point: Optional[EnRouteSegmentPoint] = field(
        default=None,
        metadata={
            "name": "EnRouteSegmentPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
