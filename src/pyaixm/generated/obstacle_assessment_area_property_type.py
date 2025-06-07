from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.obstacle_assessment_area import ObstacleAssessmentArea

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ObstacleAssessmentAreaPropertyType(AbstractAixmpropertyType):
    obstacle_assessment_area: Optional[ObstacleAssessmentArea] = field(
        default=None,
        metadata={
            "name": "ObstacleAssessmentArea",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
