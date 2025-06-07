from dataclasses import dataclass

from pyaixm.generated.obstacle_placement_type import ObstaclePlacementType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ObstaclePlacement(ObstaclePlacementType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
