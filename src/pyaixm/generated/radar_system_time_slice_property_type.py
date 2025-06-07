from dataclasses import dataclass, field
from typing import Optional

from generated.radar_system_time_slice import RadarSystemTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RadarSystemTimeSlicePropertyType:
    radar_system_time_slice: Optional[RadarSystemTimeSlice] = field(
        default=None,
        metadata={
            "name": "RadarSystemTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
