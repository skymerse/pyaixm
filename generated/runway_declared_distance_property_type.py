from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.runway_declared_distance import RunwayDeclaredDistance

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayDeclaredDistancePropertyType(AbstractAixmpropertyType):
    runway_declared_distance: Optional[RunwayDeclaredDistance] = field(
        default=None,
        metadata={
            "name": "RunwayDeclaredDistance",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
