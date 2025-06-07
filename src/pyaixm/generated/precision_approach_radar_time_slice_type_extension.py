from dataclasses import dataclass, field
from typing import Optional

from generated.precision_approach_radar_extension import (
    PrecisionApproachRadarExtension,
)
from generated.radar_equipment_extension import RadarEquipmentExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PrecisionApproachRadarTimeSliceTypeExtension:
    class Meta:
        global_type = False

    precision_approach_radar_extension: Optional[
        PrecisionApproachRadarExtension
    ] = field(
        default=None,
        metadata={
            "name": "PrecisionApproachRadarExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    radar_equipment_extension: Optional[RadarEquipmentExtension] = field(
        default=None,
        metadata={
            "name": "RadarEquipmentExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
