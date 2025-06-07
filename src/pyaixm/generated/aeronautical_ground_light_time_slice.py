from dataclasses import dataclass

from pyaixm.generated.aeronautical_ground_light_time_slice_type import (
    AeronauticalGroundLightTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AeronauticalGroundLightTimeSlice(AeronauticalGroundLightTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
