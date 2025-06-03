from dataclasses import dataclass, field
from typing import Optional, Union

from generated.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CodeLanguageType:
    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[a-z]{3}",
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
