from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.code_direction_turn_type import CodeDirectionTurnType
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.sector_design_type_extension import (
    SectorDesignTypeExtension,
)
from pyaixm.generated.val_distance_vertical_type import ValDistanceVerticalType
from pyaixm.generated.val_slope_type import ValSlopeType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SectorDesignType(AbstractAixmobjectType):
    turn_direction: Optional[CodeDirectionTurnType] = field(
        default=None,
        metadata={
            "name": "turnDirection",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    design_gradient: Optional[ValSlopeType] = field(
        default=None,
        metadata={
            "name": "designGradient",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    termination_altitude: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "terminationAltitude",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    turn_permitted: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "turnPermitted",
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
    extension: Iterable[SectorDesignTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
