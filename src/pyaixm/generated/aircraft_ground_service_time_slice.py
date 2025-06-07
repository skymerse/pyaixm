from dataclasses import dataclass

from generated.aircraft_ground_service_time_slice_type import (
    AircraftGroundServiceTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AircraftGroundServiceTimeSlice(AircraftGroundServiceTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
