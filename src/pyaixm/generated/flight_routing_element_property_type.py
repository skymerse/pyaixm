from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.flight_routing_element import FlightRoutingElement

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FlightRoutingElementPropertyType(AbstractAixmpropertyType):
    flight_routing_element: Optional[FlightRoutingElement] = field(
        default=None,
        metadata={
            "name": "FlightRoutingElement",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
