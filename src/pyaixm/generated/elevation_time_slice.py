from dataclasses import dataclass

from pyaixm.generated.elevation_time_slice_type import ElevationTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ElevationTimeSlice(ElevationTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
