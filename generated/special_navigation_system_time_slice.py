from dataclasses import dataclass

from generated.special_navigation_system_time_slice_type import (
    SpecialNavigationSystemTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SpecialNavigationSystemTimeSlice(SpecialNavigationSystemTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
