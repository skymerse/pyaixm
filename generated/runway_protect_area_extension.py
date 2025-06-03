from dataclasses import dataclass

from generated.runway_protect_area_extension_type import (
    RunwayProtectAreaExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class RunwayProtectAreaExtension(RunwayProtectAreaExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
