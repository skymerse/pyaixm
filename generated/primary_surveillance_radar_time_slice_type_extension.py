from dataclasses import dataclass, field
from typing import Optional

from generated.primary_surveillance_radar_extension import (
    PrimarySurveillanceRadarExtension,
)
from generated.radar_equipment_extension import RadarEquipmentExtension
from generated.surveillance_radar_extension import SurveillanceRadarExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PrimarySurveillanceRadarTimeSliceTypeExtension:
    class Meta:
        global_type = False

    primary_surveillance_radar_extension: Optional[
        PrimarySurveillanceRadarExtension
    ] = field(
        default=None,
        metadata={
            "name": "PrimarySurveillanceRadarExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    surveillance_radar_extension: Optional[SurveillanceRadarExtension] = field(
        default=None,
        metadata={
            "name": "SurveillanceRadarExtension",
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
