from dataclasses import dataclass

from pyaixm.generated.authority_for_special_navigation_system_type import (
    AuthorityForSpecialNavigationSystemType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AuthorityForSpecialNavigationSystem(
    AuthorityForSpecialNavigationSystemType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
