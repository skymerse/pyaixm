from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.survey_control_point_extension import (
    SurveyControlPointExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SurveyControlPointTimeSliceTypeExtension:
    class Meta:
        global_type = False

    survey_control_point_extension: Optional[SurveyControlPointExtension] = (
        field(
            default=None,
            metadata={
                "name": "SurveyControlPointExtension",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1/event",
            },
        )
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
