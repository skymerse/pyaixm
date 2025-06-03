from dataclasses import dataclass

from generated.air_traffic_management_service_time_slice_type import (
    AirTrafficManagementServiceTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirTrafficManagementServiceTimeSlice(
    AirTrafficManagementServiceTimeSliceType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
