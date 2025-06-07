from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.survey_control_point_time_slice import (
    SurveyControlPointTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SurveyControlPointTimeSlicePropertyType:
    survey_control_point_time_slice: Optional[SurveyControlPointTimeSlice] = (
        field(
            default=None,
            metadata={
                "name": "SurveyControlPointTimeSlice",
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
