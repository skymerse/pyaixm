from dataclasses import dataclass

from pyaixm.generated.deicing_area_time_slice_type import (
    DeicingAreaTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DeicingAreaTimeSlice(DeicingAreaTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
