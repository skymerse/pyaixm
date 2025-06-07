from dataclasses import dataclass

from generated.distance_indication_time_slice_type import (
    DistanceIndicationTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DistanceIndicationTimeSlice(DistanceIndicationTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
