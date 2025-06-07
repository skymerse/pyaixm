from dataclasses import dataclass

from pyaixm.generated.flight_routing_element_type import (
    FlightRoutingElementType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FlightRoutingElement(FlightRoutingElementType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
