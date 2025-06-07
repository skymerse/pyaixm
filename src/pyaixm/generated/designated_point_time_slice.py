from dataclasses import dataclass

from generated.designated_point_time_slice_type import (
    DesignatedPointTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DesignatedPointTimeSlice(DesignatedPointTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
