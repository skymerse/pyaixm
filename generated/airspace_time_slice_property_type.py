from dataclasses import dataclass, field
from typing import Optional

from generated.airspace_time_slice import AirspaceTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirspaceTimeSlicePropertyType:
    airspace_time_slice: Optional[AirspaceTimeSlice] = field(
        default=None,
        metadata={
            "name": "AirspaceTimeSlice",
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
