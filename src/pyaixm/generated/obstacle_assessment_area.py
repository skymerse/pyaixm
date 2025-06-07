from dataclasses import dataclass

from generated.obstacle_assessment_area_type import ObstacleAssessmentAreaType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ObstacleAssessmentArea(ObstacleAssessmentAreaType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
