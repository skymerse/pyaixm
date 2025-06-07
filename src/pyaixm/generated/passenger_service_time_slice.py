from dataclasses import dataclass

from pyaixm.generated.passenger_service_time_slice_type import (
    PassengerServiceTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PassengerServiceTimeSlice(PassengerServiceTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
