from dataclasses import dataclass

from generated.flight_restriction_time_slice_type import (
    FlightRestrictionTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FlightRestrictionTimeSlice(FlightRestrictionTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
