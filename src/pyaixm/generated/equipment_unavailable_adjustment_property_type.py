from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.equipment_unavailable_adjustment import (
    EquipmentUnavailableAdjustment,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class EquipmentUnavailableAdjustmentPropertyType(AbstractAixmpropertyType):
    equipment_unavailable_adjustment: Optional[
        EquipmentUnavailableAdjustment
    ] = field(
        default=None,
        metadata={
            "name": "EquipmentUnavailableAdjustment",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
