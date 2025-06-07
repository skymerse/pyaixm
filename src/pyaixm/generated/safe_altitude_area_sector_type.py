from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.circle_sector_property_type import CircleSectorPropertyType
from generated.note_property_type import NotePropertyType
from generated.obstruction_property_type import ObstructionPropertyType
from generated.safe_altitude_area_sector_type_extension import (
    SafeAltitudeAreaSectorTypeExtension,
)
from generated.surface_property_type_2 import SurfacePropertyType2
from generated.val_distance_type import ValDistanceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SafeAltitudeAreaSectorType(AbstractAixmobjectType):
    buffer_width: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "bufferWidth",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extent: Optional[SurfacePropertyType2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    significant_obstacle: Iterable[ObstructionPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "significantObstacle",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    sector_definition: Optional[CircleSectorPropertyType] = field(
        default=None,
        metadata={
            "name": "sectorDefinition",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    annotation: Iterable[NotePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[SafeAltitudeAreaSectorTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
