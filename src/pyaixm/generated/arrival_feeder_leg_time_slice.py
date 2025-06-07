from dataclasses import dataclass

from generated.arrival_feeder_leg_time_slice_type import (
    ArrivalFeederLegTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ArrivalFeederLegTimeSlice(ArrivalFeederLegTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
