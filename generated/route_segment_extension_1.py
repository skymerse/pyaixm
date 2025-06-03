from dataclasses import dataclass

from generated.route_segment_extension_type_1 import RouteSegmentExtensionType1

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class RouteSegmentExtension1(RouteSegmentExtensionType1):
    class Meta:
        name = "RouteSegmentExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
