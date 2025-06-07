from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union

from pyaixm.generated.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from pyaixm.generated.uom_speed_type_value import UomSpeedTypeValue

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ValSpeedType:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0"),
        },
    )
    uom: Optional[Union[str, UomSpeedTypeValue]] = field(
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
