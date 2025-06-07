from dataclasses import dataclass

from pyaixm.generated.road_time_slice_type import RoadTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RoadTimeSlice(RoadTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
