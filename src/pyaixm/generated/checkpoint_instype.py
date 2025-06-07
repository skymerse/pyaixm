from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_navigation_system_checkpoint_type import (
    AbstractNavigationSystemCheckpointType,
)
from pyaixm.generated.checkpoint_instime_slice_property_type import (
    CheckpointInstimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CheckpointInstype(AbstractNavigationSystemCheckpointType):
    class Meta:
        name = "CheckpointINSType"

    time_slice: Iterable[CheckpointInstimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
