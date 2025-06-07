from dataclasses import dataclass, field
from typing import Optional, Union

from pyaixm.generated.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CodeAirspaceDesignatorType:
    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "max_length": 10,
            "pattern": r'([A-Z]|[0-9]|[, !"&#$%\'\(\)\*\+\-\./:;<=>\?@\[\\\]\^_\|\{\}])*',
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
