from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.circle_sector import CircleSector

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CircleSectorPropertyType(AbstractAixmpropertyType):
    circle_sector: Optional[CircleSector] = field(
        default=None,
        metadata={
            "name": "CircleSector",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
