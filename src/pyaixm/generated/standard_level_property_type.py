from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.standard_level import StandardLevel

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardLevelPropertyType(AbstractAixmpropertyType):
    standard_level: Optional[StandardLevel] = field(
        default=None,
        metadata={
            "name": "StandardLevel",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
