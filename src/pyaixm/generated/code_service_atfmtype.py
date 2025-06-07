from dataclasses import dataclass, field
from typing import Optional, Union

from generated.code_service_atfmbase_type_value import (
    CodeServiceAtfmbaseTypeValue,
)
from generated.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CodeServiceAtfmtype:
    class Meta:
        name = "CodeServiceATFMType"

    value: Union[str, CodeServiceAtfmbaseTypeValue] = field(
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
