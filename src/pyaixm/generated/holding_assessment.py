from dataclasses import dataclass

from pyaixm.generated.holding_assessment_type import HoldingAssessmentType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class HoldingAssessment(HoldingAssessmentType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
