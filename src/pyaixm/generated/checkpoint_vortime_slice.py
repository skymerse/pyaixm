from dataclasses import dataclass

from pyaixm.generated.checkpoint_vortime_slice_type import (
    CheckpointVortimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CheckpointVortimeSlice(CheckpointVortimeSliceType):
    class Meta:
        name = "CheckpointVORTimeSlice"
        namespace = "http://www.aixm.aero/schema/5.1"
