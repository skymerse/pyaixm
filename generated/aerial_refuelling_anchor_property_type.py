from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.aerial_refuelling_anchor import AerialRefuellingAnchor

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AerialRefuellingAnchorPropertyType(AbstractAixmpropertyType):
    aerial_refuelling_anchor: Optional[AerialRefuellingAnchor] = field(
        default=None,
        metadata={
            "name": "AerialRefuellingAnchor",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
