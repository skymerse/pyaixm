from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.checkpoint_vortime_slice import CheckpointVortimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CheckpointVortimeSlicePropertyType:
    class Meta:
        name = "CheckpointVORTimeSlicePropertyType"

    checkpoint_vortime_slice: Optional[CheckpointVortimeSlice] = field(
        default=None,
        metadata={
            "name": "CheckpointVORTimeSlice",
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
