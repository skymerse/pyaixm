from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.secondary_surveillance_radar_time_slice import (
    SecondarySurveillanceRadarTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SecondarySurveillanceRadarTimeSlicePropertyType:
    secondary_surveillance_radar_time_slice: Optional[
        SecondarySurveillanceRadarTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "SecondarySurveillanceRadarTimeSlice",
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
