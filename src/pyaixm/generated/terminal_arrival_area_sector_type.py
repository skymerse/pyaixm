from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.circle_sector_property_type import (
    CircleSectorPropertyType,
)
from pyaixm.generated.code_altitude_use_type import CodeAltitudeUseType
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.obstruction_property_type import ObstructionPropertyType
from pyaixm.generated.surface_property_type_2 import SurfacePropertyType2
from pyaixm.generated.terminal_arrival_area_sector_type_extension import (
    TerminalArrivalAreaSectorTypeExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TerminalArrivalAreaSectorType(AbstractAixmobjectType):
    fly_by_code: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "flyByCode",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    procedure_turn_required: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "procedureTurnRequired",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    altitude_description: Optional[CodeAltitudeUseType] = field(
        default=None,
        metadata={
            "name": "altitudeDescription",
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
    annotation: Iterable[NotePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    extension: Iterable[TerminalArrivalAreaSectorTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
