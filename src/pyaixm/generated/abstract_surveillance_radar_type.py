from dataclasses import dataclass

from pyaixm.generated.abstract_radar_equipment_type import (
    AbstractRadarEquipmentType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractSurveillanceRadarType(AbstractRadarEquipmentType):
    pass
