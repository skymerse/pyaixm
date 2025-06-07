from dataclasses import dataclass, field
from typing import Optional, Union

from generated.code_ilsback_course_base_type_value import (
    CodeIlsbackCourseBaseTypeValue,
)
from generated.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CodeIlsbackCourseType:
    class Meta:
        name = "CodeILSBackCourseType"

    value: Union[str, CodeIlsbackCourseBaseTypeValue] = field(
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
