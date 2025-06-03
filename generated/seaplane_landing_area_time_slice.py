from dataclasses import dataclass

from generated.seaplane_landing_area_time_slice_type import (
    SeaplaneLandingAreaTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SeaplaneLandingAreaTimeSlice(SeaplaneLandingAreaTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
