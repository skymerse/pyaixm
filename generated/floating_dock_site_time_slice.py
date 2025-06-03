from dataclasses import dataclass

from generated.floating_dock_site_time_slice_type import (
    FloatingDockSiteTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FloatingDockSiteTimeSlice(FloatingDockSiteTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
