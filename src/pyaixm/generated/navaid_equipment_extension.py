from dataclasses import dataclass

from pyaixm.generated.navaid_equipment_extension_type import (
    NavaidEquipmentExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class NavaidEquipmentExtension(NavaidEquipmentExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
