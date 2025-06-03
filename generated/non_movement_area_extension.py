from dataclasses import dataclass

from generated.non_movement_area_extension_type import (
    NonMovementAreaExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class NonMovementAreaExtension(NonMovementAreaExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
