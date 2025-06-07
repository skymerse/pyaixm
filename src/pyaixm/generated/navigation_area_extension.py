from dataclasses import dataclass

from generated.navigation_area_extension_type import (
    NavigationAreaExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class NavigationAreaExtension(NavigationAreaExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
