from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.checkpoint_instime_slice import CheckpointInstimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CheckpointInstimeSlicePropertyType:
    class Meta:
        name = "CheckpointINSTimeSlicePropertyType"

    checkpoint_instime_slice: Optional[CheckpointInstimeSlice] = field(
        default=None,
        metadata={
            "name": "CheckpointINSTimeSlice",
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
