from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.holding_assessment_extension import (
    HoldingAssessmentExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class HoldingAssessmentTimeSliceTypeExtension:
    class Meta:
        global_type = False

    holding_assessment_extension: Optional[HoldingAssessmentExtension] = field(
        default=None,
        metadata={
            "name": "HoldingAssessmentExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
