from dataclasses import dataclass, field
from typing import Optional, Union

from generated.code_landing_marking_base_type import CodeLandingMarkingBaseType
from generated.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class CodeLandingMarkingType:
    value: Optional[CodeLandingMarkingBaseType] = field(
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
