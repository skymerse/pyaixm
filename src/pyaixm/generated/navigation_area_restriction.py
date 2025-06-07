from dataclasses import dataclass

from pyaixm.generated.navigation_area_restriction_type import (
    NavigationAreaRestrictionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavigationAreaRestriction(NavigationAreaRestrictionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
