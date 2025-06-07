from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.surface_characteristics import SurfaceCharacteristics

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SurfaceCharacteristicsPropertyType(AbstractAixmpropertyType):
    surface_characteristics: Optional[SurfaceCharacteristics] = field(
        default=None,
        metadata={
            "name": "SurfaceCharacteristics",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
