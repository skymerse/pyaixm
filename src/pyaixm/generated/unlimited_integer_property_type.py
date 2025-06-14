from dataclasses import dataclass, field
from typing import Optional, Union

from pyaixm.generated.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from pyaixm.generated.unlimited_integer import UnlimitedInteger

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class UnlimitedIntegerPropertyType:
    class Meta:
        name = "UnlimitedInteger_PropertyType"

    unlimited_integer: Optional[UnlimitedInteger] = field(
        default=None,
        metadata={
            "name": "UnlimitedInteger",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
            "nillable": True,
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
