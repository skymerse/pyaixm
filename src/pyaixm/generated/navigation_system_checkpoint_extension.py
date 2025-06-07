from dataclasses import dataclass

from generated.navigation_system_checkpoint_extension_type import (
    NavigationSystemCheckpointExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class NavigationSystemCheckpointExtension(
    NavigationSystemCheckpointExtensionType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
