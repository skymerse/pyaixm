from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.ground_lighting_availability import GroundLightingAvailability

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GroundLightingAvailabilityPropertyType(AbstractAixmpropertyType):
    ground_lighting_availability: Optional[GroundLightingAvailability] = field(
        default=None,
        metadata={
            "name": "GroundLightingAvailability",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
