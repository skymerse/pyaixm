from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.elevated_surface import ElevatedSurface

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ElevatedSurfacePropertyType(AbstractAixmpropertyType):
    elevated_surface: Optional[ElevatedSurface] = field(
        default=None,
        metadata={
            "name": "ElevatedSurface",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
