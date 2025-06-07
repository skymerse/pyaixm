from dataclasses import dataclass

from pyaixm.generated.holding_assessment_time_slice_type import (
    HoldingAssessmentTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class HoldingAssessmentTimeSlice(HoldingAssessmentTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
