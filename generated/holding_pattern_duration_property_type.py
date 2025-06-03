from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.holding_pattern_duration import HoldingPatternDuration

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class HoldingPatternDurationPropertyType(AbstractAixmpropertyType):
    holding_pattern_duration: Optional[HoldingPatternDuration] = field(
        default=None,
        metadata={
            "name": "HoldingPatternDuration",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
