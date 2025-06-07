from dataclasses import dataclass, field
from typing import Optional

from generated.holding_assessment_time_slice import HoldingAssessmentTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class HoldingAssessmentTimeSlicePropertyType:
    holding_assessment_time_slice: Optional[HoldingAssessmentTimeSlice] = (
        field(
            default=None,
            metadata={
                "name": "HoldingAssessmentTimeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "required": True,
            },
        )
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
