from dataclasses import dataclass

from generated.navigation_area_type import NavigationAreaType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavigationArea(NavigationAreaType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
