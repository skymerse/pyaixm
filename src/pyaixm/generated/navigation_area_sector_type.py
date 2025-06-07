from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.circle_sector_property_type import (
    CircleSectorPropertyType,
)
from pyaixm.generated.navigation_area_sector_type_extension import (
    NavigationAreaSectorTypeExtension,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.obstruction_property_type import ObstructionPropertyType
from pyaixm.generated.sector_design_property_type import (
    SectorDesignPropertyType,
)
from pyaixm.generated.surface_property_type_2 import SurfacePropertyType2

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavigationAreaSectorType(AbstractAixmobjectType):
    sector_definition: Optional[CircleSectorPropertyType] = field(
        default=None,
        metadata={
            "name": "sectorDefinition",
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
    extent: Optional[SurfacePropertyType2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    sector_criteria: Iterable[SectorDesignPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "sectorCriteria",
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
    extension: Iterable[NavigationAreaSectorTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
