from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.abstract_aixmproperty_type import (
    AbstractAixmpropertyType,
)
from pyaixm.generated.equipment_unavailable_adjustment import (
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
