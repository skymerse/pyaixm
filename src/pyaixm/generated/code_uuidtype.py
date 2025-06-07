from dataclasses import dataclass, field
from typing import Optional, Union

from pyaixm.generated.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CodeUuidtype:
    class Meta:
        name = "CodeUUIDType"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"([A-F]|[a-f]|\d|\-)*",
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
