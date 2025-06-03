from dataclasses import dataclass

from generated.aircraft_stand_time_slice_type import AircraftStandTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AircraftStandTimeSlice(AircraftStandTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
