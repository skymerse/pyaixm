from dataclasses import dataclass

from pyaixm.generated.aerial_refuelling_time_slice_type import (
    AerialRefuellingTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AerialRefuellingTimeSlice(AerialRefuellingTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
