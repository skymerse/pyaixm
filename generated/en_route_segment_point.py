from dataclasses import dataclass

from generated.en_route_segment_point_type import EnRouteSegmentPointType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class EnRouteSegmentPoint(EnRouteSegmentPointType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
