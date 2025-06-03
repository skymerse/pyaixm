from dataclasses import dataclass

from generated.route_type import RouteType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class Route(RouteType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
