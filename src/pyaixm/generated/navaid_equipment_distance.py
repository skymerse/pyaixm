from dataclasses import dataclass

from pyaixm.generated.navaid_equipment_distance_type import (
    NavaidEquipmentDistanceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavaidEquipmentDistance(NavaidEquipmentDistanceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
