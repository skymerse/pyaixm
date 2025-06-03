from dataclasses import dataclass

from generated.navaid_equipment_monitoring_type import (
    NavaidEquipmentMonitoringType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavaidEquipmentMonitoring(NavaidEquipmentMonitoringType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
