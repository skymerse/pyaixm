from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.equipment_unavailable_adjustment_column import (
    EquipmentUnavailableAdjustmentColumn,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class EquipmentUnavailableAdjustmentColumnPropertyType(
    AbstractAixmpropertyType
):
    equipment_unavailable_adjustment_column: Optional[
        EquipmentUnavailableAdjustmentColumn
    ] = field(
        default=None,
        metadata={
            "name": "EquipmentUnavailableAdjustmentColumn",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
