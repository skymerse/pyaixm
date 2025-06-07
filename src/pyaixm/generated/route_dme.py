from dataclasses import dataclass

from generated.route_dmetype import RouteDmetype

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RouteDme(RouteDmetype):
    class Meta:
        name = "RouteDME"
        namespace = "http://www.aixm.aero/schema/5.1"
