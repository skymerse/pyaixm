from dataclasses import dataclass

from pyaixm.generated.checkpoint_instime_slice_type import (
    CheckpointInstimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CheckpointInstimeSlice(CheckpointInstimeSliceType):
    class Meta:
        name = "CheckpointINSTimeSlice"
        namespace = "http://www.aixm.aero/schema/5.1"
