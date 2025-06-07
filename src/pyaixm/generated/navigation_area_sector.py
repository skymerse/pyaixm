from dataclasses import dataclass

from pyaixm.generated.navigation_area_sector_type import (
    NavigationAreaSectorType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavigationAreaSector(NavigationAreaSectorType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
