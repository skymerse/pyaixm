from dataclasses import dataclass

from generated.airport_heliport_time_slice_type import (
    AirportHeliportTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportHeliportTimeSlice(AirportHeliportTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
