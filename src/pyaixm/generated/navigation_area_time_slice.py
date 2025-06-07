from dataclasses import dataclass

from pyaixm.generated.navigation_area_time_slice_type import (
    NavigationAreaTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavigationAreaTimeSlice(NavigationAreaTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
