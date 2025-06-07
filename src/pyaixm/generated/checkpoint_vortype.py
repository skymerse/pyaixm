from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_navigation_system_checkpoint_type import (
    AbstractNavigationSystemCheckpointType,
)
from pyaixm.generated.checkpoint_vortime_slice_property_type import (
    CheckpointVortimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CheckpointVortype(AbstractNavigationSystemCheckpointType):
    class Meta:
        name = "CheckpointVORType"

    time_slice: Iterable[CheckpointVortimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
