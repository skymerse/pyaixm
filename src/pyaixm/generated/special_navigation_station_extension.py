from dataclasses import dataclass

from pyaixm.generated.special_navigation_station_extension_type import (
    SpecialNavigationStationExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class SpecialNavigationStationExtension(SpecialNavigationStationExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
