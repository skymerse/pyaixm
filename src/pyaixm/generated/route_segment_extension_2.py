from dataclasses import dataclass

from generated.route_segment_extension_type_2 import RouteSegmentExtensionType2

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class RouteSegmentExtension2(RouteSegmentExtensionType2):
    class Meta:
        name = "RouteSegmentExtension"
        namespace = "urn:us.gov.dot.faa.aim.fns"
