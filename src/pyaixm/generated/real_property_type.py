from dataclasses import dataclass, field
from typing import Optional, Union

from pyaixm.generated.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from pyaixm.generated.real import Real

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class RealPropertyType:
    class Meta:
        name = "Real_PropertyType"

    real: Optional[Real] = field(
        default=None,
        metadata={
            "name": "Real",
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
