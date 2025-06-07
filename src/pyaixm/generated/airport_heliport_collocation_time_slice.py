from dataclasses import dataclass

from generated.airport_heliport_collocation_time_slice_type import (
    AirportHeliportCollocationTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportHeliportCollocationTimeSlice(
    AirportHeliportCollocationTimeSliceType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
