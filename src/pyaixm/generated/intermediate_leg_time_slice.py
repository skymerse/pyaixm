from dataclasses import dataclass

from generated.intermediate_leg_time_slice_type import (
    IntermediateLegTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class IntermediateLegTimeSlice(IntermediateLegTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
