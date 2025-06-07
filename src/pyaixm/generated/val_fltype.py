from dataclasses import dataclass, field
from typing import Optional, Union

from generated.nil_reason_enumeration_value import NilReasonEnumerationValue
from generated.uom_fltype_value import UomFltypeValue

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ValFltype:
    class Meta:
        name = "ValFLType"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": 999,
        },
    )
    uom: Optional[Union[str, UomFltypeValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
