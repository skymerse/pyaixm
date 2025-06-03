from dataclasses import dataclass

from generated.equipment_unavailable_adjustment_type import (
    EquipmentUnavailableAdjustmentType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class EquipmentUnavailableAdjustment(EquipmentUnavailableAdjustmentType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
