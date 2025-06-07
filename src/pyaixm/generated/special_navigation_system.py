from dataclasses import dataclass

from generated.special_navigation_system_type import (
    SpecialNavigationSystemType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SpecialNavigationSystem(SpecialNavigationSystemType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
