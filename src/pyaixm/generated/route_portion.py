from dataclasses import dataclass

from generated.route_portion_type import RoutePortionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RoutePortion(RoutePortionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
