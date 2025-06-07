from dataclasses import dataclass, field
from typing import Optional, Union

from generated.decimal import DecimalType
from generated.integer import Integer
from generated.nil_reason_enumeration_value import NilReasonEnumerationValue
from generated.real import Real

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class NumberPropertyType:
    class Meta:
        name = "Number_PropertyType"

    real: Optional[Real] = field(
        default=None,
        metadata={
            "name": "Real",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
        },
    )
    decimal: Optional[DecimalType] = field(
        default=None,
        metadata={
            "name": "Decimal",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
        },
    )
    integer: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "Integer",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        },
    )
