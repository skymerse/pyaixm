from dataclasses import dataclass, field
from typing import Optional

from generated.glidepath_time_slice import GlidepathTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GlidepathTimeSlicePropertyType:
    glidepath_time_slice: Optional[GlidepathTimeSlice] = field(
        default=None,
        metadata={
            "name": "GlidepathTimeSlice",
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
