from dataclasses import dataclass

from generated.airport_supplies_service_time_slice_type import (
    AirportSuppliesServiceTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportSuppliesServiceTimeSlice(AirportSuppliesServiceTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
