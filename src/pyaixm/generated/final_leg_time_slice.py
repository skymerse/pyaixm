from dataclasses import dataclass

from pyaixm.generated.final_leg_time_slice_type import FinalLegTimeSliceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FinalLegTimeSlice(FinalLegTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
