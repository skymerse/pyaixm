from dataclasses import dataclass

from pyaixm.generated.air_traffic_control_service_time_slice_type import (
    AirTrafficControlServiceTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirTrafficControlServiceTimeSlice(AirTrafficControlServiceTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
