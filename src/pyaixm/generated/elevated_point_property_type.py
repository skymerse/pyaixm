from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.elevated_point import ElevatedPoint

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ElevatedPointPropertyType(AbstractAixmpropertyType):
    elevated_point: Optional[ElevatedPoint] = field(
        default=None,
        metadata={
            "name": "ElevatedPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
