from dataclasses import dataclass

from pyaixm.generated.route_dmetime_slice_type import RouteDmetimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RouteDmetimeSlice(RouteDmetimeSliceType):
    class Meta:
        name = "RouteDMETimeSlice"
        namespace = "http://www.aixm.aero/schema/5.1"
