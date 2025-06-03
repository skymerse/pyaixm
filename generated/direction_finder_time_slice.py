from dataclasses import dataclass

from generated.direction_finder_time_slice_type import (
    DirectionFinderTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DirectionFinderTimeSlice(DirectionFinderTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
