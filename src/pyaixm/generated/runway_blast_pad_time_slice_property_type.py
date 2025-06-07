from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.runway_blast_pad_time_slice import (
    RunwayBlastPadTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayBlastPadTimeSlicePropertyType:
    runway_blast_pad_time_slice: Optional[RunwayBlastPadTimeSlice] = field(
        default=None,
        metadata={
            "name": "RunwayBlastPadTimeSlice",
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
