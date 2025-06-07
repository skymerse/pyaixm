from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.obstruction import Obstruction

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ObstructionPropertyType(AbstractAixmpropertyType):
    obstruction: Optional[Obstruction] = field(
        default=None,
        metadata={
            "name": "Obstruction",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
