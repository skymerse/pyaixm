from dataclasses import dataclass

from generated.safe_altitude_area_time_slice_type import (
    SafeAltitudeAreaTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SafeAltitudeAreaTimeSlice(SafeAltitudeAreaTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
