from dataclasses import dataclass

from generated.route_extension_type import RouteExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class RouteExtension(RouteExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
