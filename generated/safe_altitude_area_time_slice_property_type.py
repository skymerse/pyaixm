from dataclasses import dataclass, field
from typing import Optional

from generated.safe_altitude_area_time_slice import SafeAltitudeAreaTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SafeAltitudeAreaTimeSlicePropertyType:
    safe_altitude_area_time_slice: Optional[SafeAltitudeAreaTimeSlice] = field(
        default=None,
        metadata={
            "name": "SafeAltitudeAreaTimeSlice",
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
