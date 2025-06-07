from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.circling_restriction import CirclingRestriction

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CirclingRestrictionPropertyType(AbstractAixmpropertyType):
    circling_restriction: Optional[CirclingRestriction] = field(
        default=None,
        metadata={
            "name": "CirclingRestriction",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
