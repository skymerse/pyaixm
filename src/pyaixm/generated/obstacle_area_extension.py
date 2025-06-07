from dataclasses import dataclass

from pyaixm.generated.obstacle_area_extension_type import (
    ObstacleAreaExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class ObstacleAreaExtension(ObstacleAreaExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
