from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.obstacle_placement import ObstaclePlacement

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ObstaclePlacementPropertyType(AbstractAixmpropertyType):
    obstacle_placement: Optional[ObstaclePlacement] = field(
        default=None,
        metadata={
            "name": "ObstaclePlacement",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
