from dataclasses import dataclass

from pyaixm.generated.abstract_navigation_system_checkpoint_type import (
    AbstractNavigationSystemCheckpointType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractNavigationSystemCheckpoint(
    AbstractNavigationSystemCheckpointType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
