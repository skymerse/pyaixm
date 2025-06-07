from dataclasses import dataclass

from pyaixm.generated.authority_for_special_navigation_station_type import (
    AuthorityForSpecialNavigationStationType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AuthorityForSpecialNavigationStation(
    AuthorityForSpecialNavigationStationType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
