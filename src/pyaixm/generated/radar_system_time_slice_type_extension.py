from dataclasses import dataclass, field
from typing import Optional

from generated.radar_system_extension import RadarSystemExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RadarSystemTimeSliceTypeExtension:
    class Meta:
        global_type = False

    radar_system_extension: Optional[RadarSystemExtension] = field(
        default=None,
        metadata={
            "name": "RadarSystemExtension",
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
