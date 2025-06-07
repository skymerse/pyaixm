from dataclasses import dataclass, field
from typing import Optional

from generated.runway_centreline_point_time_slice import (
    RunwayCentrelinePointTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayCentrelinePointTimeSlicePropertyType:
    runway_centreline_point_time_slice: Optional[
        RunwayCentrelinePointTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "RunwayCentrelinePointTimeSlice",
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
