from dataclasses import dataclass

from generated.radar_equipment_extension_type import (
    RadarEquipmentExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class RadarEquipmentExtension(RadarEquipmentExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
