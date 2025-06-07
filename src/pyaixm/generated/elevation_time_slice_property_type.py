from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.elevation_time_slice import ElevationTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ElevationTimeSlicePropertyType:
    elevation_time_slice: Optional[ElevationTimeSlice] = field(
        default=None,
        metadata={
            "name": "ElevationTimeSlice",
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
