from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.altitude_adjustment_property_type import (
    AltitudeAdjustmentPropertyType,
)
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.obstacle_placement_property_type import (
    ObstaclePlacementPropertyType,
)
from pyaixm.generated.obstruction_type_extension import (
    ObstructionTypeExtension,
)
from pyaixm.generated.val_angle_type import ValAngleType
from pyaixm.generated.val_distance_type import ValDistanceType
from pyaixm.generated.val_distance_vertical_type import ValDistanceVerticalType
from pyaixm.generated.vertical_structure_property_type import (
    VerticalStructurePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ObstructionType(AbstractAixmobjectType):
    required_clearance: Optional[ValDistanceType] = field(
        default=None,
        metadata={
            "name": "requiredClearance",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    minimum_altitude: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "minimumAltitude",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    surface_penetration: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "surfacePenetration",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    slope_penetration: Optional[ValAngleType] = field(
        default=None,
        metadata={
            "name": "slopePenetration",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    controlling: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    close_in: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "closeIn",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    the_vertical_structure: Optional[VerticalStructurePropertyType] = field(
        default=None,
        metadata={
            "name": "theVerticalStructure",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    adjustment: Iterable[AltitudeAdjustmentPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    obstacle_placement: Iterable[ObstaclePlacementPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "obstaclePlacement",
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
    extension: Iterable[ObstructionTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
