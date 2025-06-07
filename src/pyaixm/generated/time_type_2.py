from dataclasses import dataclass, field
from typing import Optional, Union

from pyaixm.generated.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TimeType2:
    class Meta:
        name = "TimeType"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"(([0-1][0-9]|2[0-3]):[0-5][0-9])|(24:00)",
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
