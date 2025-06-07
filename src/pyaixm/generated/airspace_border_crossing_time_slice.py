from dataclasses import dataclass

from pyaixm.generated.airspace_border_crossing_time_slice_type import (
    AirspaceBorderCrossingTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirspaceBorderCrossingTimeSlice(AirspaceBorderCrossingTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
