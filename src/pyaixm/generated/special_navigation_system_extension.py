from dataclasses import dataclass

from generated.special_navigation_system_extension_type import (
    SpecialNavigationSystemExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class SpecialNavigationSystemExtension(SpecialNavigationSystemExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
