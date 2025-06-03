from dataclasses import dataclass

from generated.holding_assessment_extension_type import (
    HoldingAssessmentExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class HoldingAssessmentExtension(HoldingAssessmentExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
