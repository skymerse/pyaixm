from dataclasses import dataclass, field
from typing import Optional, Union

from generated.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CodeRnptype:
    class Meta:
        name = "CodeRNPType"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[0-9]{1,2}(\.[0-9]{1}){0,1}",
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
