from dataclasses import dataclass

from generated.airport_hot_spot_time_slice_type import (
    AirportHotSpotTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportHotSpotTimeSlice(AirportHotSpotTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
