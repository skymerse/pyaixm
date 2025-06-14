from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_object_type import AbstractObjectType
from pyaixm.generated.integer_property_type import IntegerPropertyType
from pyaixm.generated.unlimited_integer_property_type import (
    UnlimitedIntegerPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class MultiplicityRangeType(AbstractObjectType):
    """
    A component of a multiplicity, consisting of an non-negative lower bound, and a
    potentially infinite upper bound.
    """

    class Meta:
        name = "MultiplicityRange_Type"

    lower: Optional[IntegerPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
            "required": True,
        },
    )
    upper: Optional[UnlimitedIntegerPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
            "required": True,
        },
    )
