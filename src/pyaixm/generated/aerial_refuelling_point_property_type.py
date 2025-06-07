from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.aerial_refuelling_point import AerialRefuellingPoint

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AerialRefuellingPointPropertyType(AbstractAixmpropertyType):
    aerial_refuelling_point: Optional[AerialRefuellingPoint] = field(
        default=None,
        metadata={
            "name": "AerialRefuellingPoint",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
