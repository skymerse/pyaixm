from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.elevated_surface import ElevatedSurface
from pyaixm.generated.surface_2 import Surface2

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SurfacePropertyType2(AbstractAixmpropertyType):
    class Meta:
        name = "SurfacePropertyType"

    elevated_surface: Optional[ElevatedSurface] = field(
        default=None,
        metadata={
            "name": "ElevatedSurface",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
    surface: Optional[Surface2] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
