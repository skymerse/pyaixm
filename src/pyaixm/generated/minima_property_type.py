from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.minima import Minima

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class MinimaPropertyType(AbstractAixmpropertyType):
    minima: Optional[Minima] = field(
        default=None,
        metadata={
            "name": "Minima",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
