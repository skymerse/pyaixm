from dataclasses import dataclass, field
from typing import Optional, Union

from generated.distance import Distance
from generated.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class DistancePropertyType:
    class Meta:
        name = "Distance_PropertyType"

    distance: Optional[Distance] = field(
        default=None,
        metadata={
            "name": "Distance",
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
