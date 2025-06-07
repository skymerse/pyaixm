from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union

from generated.nil_reason_enumeration_value import NilReasonEnumerationValue
from generated.uom_frequency_type_value import UomFrequencyTypeValue

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ValFrequencyType:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": Decimal("0"),
        },
    )
    uom: Optional[Union[str, UomFrequencyTypeValue]] = field(
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
