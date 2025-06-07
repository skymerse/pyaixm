from dataclasses import dataclass, field
from typing import Optional

from generated.altimeter_source_time_slice import AltimeterSourceTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AltimeterSourceTimeSlicePropertyType:
    altimeter_source_time_slice: Optional[AltimeterSourceTimeSlice] = field(
        default=None,
        metadata={
            "name": "AltimeterSourceTimeSlice",
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
