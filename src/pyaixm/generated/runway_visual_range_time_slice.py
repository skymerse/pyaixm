from dataclasses import dataclass

from pyaixm.generated.runway_visual_range_time_slice_type import (
    RunwayVisualRangeTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayVisualRangeTimeSlice(RunwayVisualRangeTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
