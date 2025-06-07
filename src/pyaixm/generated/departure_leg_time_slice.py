from dataclasses import dataclass

from generated.departure_leg_time_slice_type import DepartureLegTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DepartureLegTimeSlice(DepartureLegTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
