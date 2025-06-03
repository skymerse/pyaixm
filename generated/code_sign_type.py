from dataclasses import dataclass, field
from typing import Optional, Union

from generated.code_sign_base_type import CodeSignBaseType
from generated.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class CodeSignType:
    value: Optional[CodeSignBaseType] = field(
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
