from dataclasses import dataclass

from generated.navigation_area_restriction_extension_type import (
    NavigationAreaRestrictionExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class NavigationAreaRestrictionExtension(
    NavigationAreaRestrictionExtensionType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
