from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmobject_type import AbstractAixmobjectType
from pyaixm.generated.code_approach_type import CodeApproachType
from pyaixm.generated.code_yes_no_type import CodeYesNoType
from pyaixm.generated.equipment_unavailable_adjustment_column_type_extension import (
    EquipmentUnavailableAdjustmentColumnTypeExtension,
)
from pyaixm.generated.note_property_type import NotePropertyType
from pyaixm.generated.val_distance_vertical_type import ValDistanceVerticalType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class EquipmentUnavailableAdjustmentColumnType(AbstractAixmobjectType):
    guidance_equipment: Optional[CodeApproachType] = field(
        default=None,
        metadata={
            "name": "guidanceEquipment",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    landing_system_lights: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "landingSystemLights",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    equipment_rvr: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "equipmentRVR",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    visibility_adjustment: Optional[ValDistanceVerticalType] = field(
        default=None,
        metadata={
            "name": "visibilityAdjustment",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "nillable": True,
        },
    )
    approach_lighting_inoperative: Optional[CodeYesNoType] = field(
        default=None,
        metadata={
            "name": "approachLightingInoperative",
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
    extension: Iterable[EquipmentUnavailableAdjustmentColumnTypeExtension] = (
        field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
            },
        )
    )
