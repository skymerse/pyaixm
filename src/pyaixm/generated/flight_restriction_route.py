from dataclasses import dataclass

from generated.flight_restriction_route_type import FlightRestrictionRouteType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FlightRestrictionRoute(FlightRestrictionRouteType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
