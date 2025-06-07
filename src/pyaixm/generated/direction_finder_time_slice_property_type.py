from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.direction_finder_time_slice import (
    DirectionFinderTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DirectionFinderTimeSlicePropertyType:
    direction_finder_time_slice: Optional[DirectionFinderTimeSlice] = field(
        default=None,
        metadata={
            "name": "DirectionFinderTimeSlice",
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
