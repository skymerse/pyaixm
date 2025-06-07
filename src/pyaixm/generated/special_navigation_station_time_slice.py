from dataclasses import dataclass

from generated.special_navigation_station_time_slice_type import (
    SpecialNavigationStationTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SpecialNavigationStationTimeSlice(SpecialNavigationStationTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
