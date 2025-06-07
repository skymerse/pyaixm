from dataclasses import dataclass

from pyaixm.generated.route_availability_type import RouteAvailabilityType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RouteAvailability(RouteAvailabilityType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
