from dataclasses import dataclass, field
from typing import Optional, Union

from pyaixm.generated.code_course_quality_ilsbase_type_value import (
    CodeCourseQualityIlsbaseTypeValue,
)
from pyaixm.generated.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CodeCourseQualityIlstype:
    class Meta:
        name = "CodeCourseQualityILSType"

    value: Union[str, CodeCourseQualityIlsbaseTypeValue] = field(
        default="",
        metadata={
            "pattern": r"OTHER(:(\w|_){1,58})?",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        },
    )
