from dataclasses import dataclass

from generated.initial_leg_time_slice_type import InitialLegTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class InitialLegTimeSlice(InitialLegTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
