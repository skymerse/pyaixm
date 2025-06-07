from dataclasses import dataclass

from pyaixm.generated.navigation_area_restriction_time_slice_type import (
    NavigationAreaRestrictionTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavigationAreaRestrictionTimeSlice(
    NavigationAreaRestrictionTimeSliceType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
