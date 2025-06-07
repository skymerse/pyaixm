from dataclasses import dataclass

from generated.obstacle_area_time_slice_type import ObstacleAreaTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ObstacleAreaTimeSlice(ObstacleAreaTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
