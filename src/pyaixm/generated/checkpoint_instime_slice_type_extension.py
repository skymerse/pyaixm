from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.checkpoint_insextension import CheckpointInsextension
from pyaixm.generated.navigation_system_checkpoint_extension import (
    NavigationSystemCheckpointExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CheckpointInstimeSliceTypeExtension:
    class Meta:
        global_type = False

    checkpoint_insextension: Optional[CheckpointInsextension] = field(
        default=None,
        metadata={
            "name": "CheckpointINSExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    navigation_system_checkpoint_extension: Optional[
        NavigationSystemCheckpointExtension
    ] = field(
        default=None,
        metadata={
            "name": "NavigationSystemCheckpointExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
