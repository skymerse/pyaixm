from dataclasses import dataclass

from pyaixm.generated.survey_control_point_time_slice_type import (
    SurveyControlPointTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SurveyControlPointTimeSlice(SurveyControlPointTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
