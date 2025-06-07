from dataclasses import dataclass

from generated.airport_clearance_service_time_slice_type import (
    AirportClearanceServiceTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportClearanceServiceTimeSlice(AirportClearanceServiceTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
