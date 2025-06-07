from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.route_availability import RouteAvailability

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RouteAvailabilityPropertyType(AbstractAixmpropertyType):
    route_availability: Optional[RouteAvailability] = field(
        default=None,
        metadata={
            "name": "RouteAvailability",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
