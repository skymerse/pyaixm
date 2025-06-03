from dataclasses import dataclass

from generated.survey_control_point_type import SurveyControlPointType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SurveyControlPoint(SurveyControlPointType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
