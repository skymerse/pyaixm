from dataclasses import dataclass

from pyaixm.generated.survey_control_point_extension_type import (
    SurveyControlPointExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class SurveyControlPointExtension(SurveyControlPointExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
