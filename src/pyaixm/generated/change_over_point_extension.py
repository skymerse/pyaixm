from dataclasses import dataclass

from generated.change_over_point_extension_type import (
    ChangeOverPointExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class ChangeOverPointExtension(ChangeOverPointExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
