from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.oxygen import Oxygen

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class OxygenPropertyType(AbstractAixmpropertyType):
    oxygen: Optional[Oxygen] = field(
        default=None,
        metadata={
            "name": "Oxygen",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
