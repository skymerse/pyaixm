from dataclasses import dataclass

from generated.obstacle_area_type import ObstacleAreaType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ObstacleArea(ObstacleAreaType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
