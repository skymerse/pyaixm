from dataclasses import dataclass

from generated.abstract_navaid_equipment_type import (
    AbstractNavaidEquipmentType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractNavaidEquipment(AbstractNavaidEquipmentType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
