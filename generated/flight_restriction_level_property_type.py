from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.flight_restriction_level import FlightRestrictionLevel

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FlightRestrictionLevelPropertyType(AbstractAixmpropertyType):
    flight_restriction_level: Optional[FlightRestrictionLevel] = field(
        default=None,
        metadata={
            "name": "FlightRestrictionLevel",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
