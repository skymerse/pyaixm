from dataclasses import dataclass, field
from typing import Optional

from generated.checkpoint_vorextension import CheckpointVorextension
from generated.navigation_system_checkpoint_extension import (
    NavigationSystemCheckpointExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CheckpointVortimeSliceTypeExtension:
    class Meta:
        global_type = False

    checkpoint_vorextension: Optional[CheckpointVorextension] = field(
        default=None,
        metadata={
            "name": "CheckpointVORExtension",
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
