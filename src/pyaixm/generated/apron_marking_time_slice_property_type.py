from dataclasses import dataclass, field
from typing import Optional

from generated.apron_marking_time_slice import ApronMarkingTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApronMarkingTimeSlicePropertyType:
    apron_marking_time_slice: Optional[ApronMarkingTimeSlice] = field(
        default=None,
        metadata={
            "name": "ApronMarkingTimeSlice",
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
