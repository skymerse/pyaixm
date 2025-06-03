from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.holding_pattern_distance import HoldingPatternDistance

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class HoldingPatternDistancePropertyType(AbstractAixmpropertyType):
    holding_pattern_distance: Optional[HoldingPatternDistance] = field(
        default=None,
        metadata={
            "name": "HoldingPatternDistance",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
