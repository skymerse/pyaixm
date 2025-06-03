from dataclasses import dataclass

from generated.special_navigation_station_status_type import (
    SpecialNavigationStationStatusType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SpecialNavigationStationStatus(SpecialNavigationStationStatusType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
