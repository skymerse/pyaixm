from dataclasses import dataclass, field
from typing import Optional, Union

from pyaixm.generated.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from pyaixm.generated.scoped_name import ScopedName

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class ScopedNamePropertyType:
    class Meta:
        name = "ScopedName_PropertyType"

    scoped_name: Optional[ScopedName] = field(
        default=None,
        metadata={
            "name": "ScopedName",
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
