from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.primary_surveillance_radar_time_slice import (
    PrimarySurveillanceRadarTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PrimarySurveillanceRadarTimeSlicePropertyType:
    primary_surveillance_radar_time_slice: Optional[
        PrimarySurveillanceRadarTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "PrimarySurveillanceRadarTimeSlice",
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
