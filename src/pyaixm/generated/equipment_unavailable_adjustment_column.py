from dataclasses import dataclass

from generated.equipment_unavailable_adjustment_column_type import (
    EquipmentUnavailableAdjustmentColumnType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class EquipmentUnavailableAdjustmentColumn(
    EquipmentUnavailableAdjustmentColumnType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
