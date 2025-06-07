from dataclasses import dataclass

from pyaixm.generated.arrival_leg_time_slice_type import (
    ArrivalLegTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ArrivalLegTimeSlice(ArrivalLegTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
