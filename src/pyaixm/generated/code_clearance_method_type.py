from dataclasses import dataclass, field
from typing import Optional, Union

from pyaixm.generated.code_clearance_method_base_type import (
    CodeClearanceMethodBaseType,
)
from pyaixm.generated.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class CodeClearanceMethodType:
    value: Optional[CodeClearanceMethodBaseType] = field(
        default=None,
        metadata={
            "required": True,
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
