from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.flight_restriction_route import FlightRestrictionRoute

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FlightRestrictionRoutePropertyType(AbstractAixmpropertyType):
    flight_restriction_route: Optional[FlightRestrictionRoute] = field(
        default=None,
        metadata={
            "name": "FlightRestrictionRoute",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
