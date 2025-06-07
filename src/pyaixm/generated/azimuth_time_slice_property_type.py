from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.azimuth_time_slice import AzimuthTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AzimuthTimeSlicePropertyType:
    azimuth_time_slice: Optional[AzimuthTimeSlice] = field(
        default=None,
        metadata={
            "name": "AzimuthTimeSlice",
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
