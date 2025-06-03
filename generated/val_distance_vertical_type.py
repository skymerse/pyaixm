from dataclasses import dataclass, field
from typing import Optional, Union

from generated.nil_reason_enumeration_value import NilReasonEnumerationValue
from generated.uom_distance_vertical_type_value import (
    UomDistanceVerticalTypeValue,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ValDistanceVerticalType:
    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"((\+|\-){0,1}[0-9]{1,8}(\.[0-9]{1,4}){0,1})|UNL|GND|FLOOR|CEILING",
        },
    )
    uom: Optional[Union[str, UomDistanceVerticalTypeValue]] = field(
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
