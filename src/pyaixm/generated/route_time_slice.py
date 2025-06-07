from dataclasses import dataclass

from generated.route_time_slice_type import RouteTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RouteTimeSlice(RouteTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
