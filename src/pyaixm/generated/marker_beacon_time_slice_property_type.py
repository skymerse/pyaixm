from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.marker_beacon_time_slice import MarkerBeaconTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class MarkerBeaconTimeSlicePropertyType:
    marker_beacon_time_slice: Optional[MarkerBeaconTimeSlice] = field(
        default=None,
        metadata={
            "name": "MarkerBeaconTimeSlice",
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
