from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmobject_type import AbstractAixmobjectType
from generated.code_equipment_unavailable_type import (
    CodeEquipmentUnavailableType,
)
from generated.code_yes_no_type import CodeYesNoType
from generated.equipment_unavailable_adjustment_column_property_type import (
    EquipmentUnavailableAdjustmentColumnPropertyType,
)
from generated.equipment_unavailable_adjustment_type_extension import (
    EquipmentUnavailableAdjustmentTypeExtension,
)
from generated.note_property_type import NotePropertyType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class EquipmentUnavailableAdjustmentType(AbstractAixmobjectType):
    type_value: Optional[CodeEquipmentUnavailableType] = field(
        default=None,
        metadata={
            "name": "type",
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
    adjustment_inopcol: Iterable[
        EquipmentUnavailableAdjustmentColumnPropertyType
    ] = field(
        default_factory=list,
        metadata={
            "name": "adjustmentINOPCol",
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
    extension: Iterable[EquipmentUnavailableAdjustmentTypeExtension] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
        },
    )
