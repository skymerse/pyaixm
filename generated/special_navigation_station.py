from dataclasses import dataclass

from generated.special_navigation_station_type import (
    SpecialNavigationStationType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SpecialNavigationStation(SpecialNavigationStationType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
