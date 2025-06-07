from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.obstacle_placement import ObstaclePlacement

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
