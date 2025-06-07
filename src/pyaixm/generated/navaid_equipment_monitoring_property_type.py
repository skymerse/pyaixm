from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_aixmproperty_type import AbstractAixmpropertyType
from generated.navaid_equipment_monitoring import NavaidEquipmentMonitoring

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavaidEquipmentMonitoringPropertyType(AbstractAixmpropertyType):
    navaid_equipment_monitoring: Optional[NavaidEquipmentMonitoring] = field(
        default=None,
        metadata={
            "name": "NavaidEquipmentMonitoring",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
