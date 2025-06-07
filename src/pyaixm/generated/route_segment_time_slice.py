from dataclasses import dataclass

from pyaixm.generated.route_segment_time_slice_type import (
    RouteSegmentTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RouteSegmentTimeSlice(RouteSegmentTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
