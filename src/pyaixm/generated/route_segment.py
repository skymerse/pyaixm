from dataclasses import dataclass

from pyaixm.generated.route_segment_type import RouteSegmentType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RouteSegment(RouteSegmentType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
