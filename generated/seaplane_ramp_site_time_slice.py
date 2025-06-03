from dataclasses import dataclass

from generated.seaplane_ramp_site_time_slice_type import (
    SeaplaneRampSiteTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SeaplaneRampSiteTimeSlice(SeaplaneRampSiteTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
