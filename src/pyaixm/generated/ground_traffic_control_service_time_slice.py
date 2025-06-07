from dataclasses import dataclass

from generated.ground_traffic_control_service_time_slice_type import (
    GroundTrafficControlServiceTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GroundTrafficControlServiceTimeSlice(
    GroundTrafficControlServiceTimeSliceType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
