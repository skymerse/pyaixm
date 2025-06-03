from dataclasses import dataclass, field
from typing import Optional

from generated.runway_element_time_slice import RunwayElementTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayElementTimeSlicePropertyType:
    runway_element_time_slice: Optional[RunwayElementTimeSlice] = field(
        default=None,
        metadata={
            "name": "RunwayElementTimeSlice",
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
