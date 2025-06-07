from dataclasses import dataclass

from pyaixm.generated.runway_centreline_point_time_slice_type import (
    RunwayCentrelinePointTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayCentrelinePointTimeSlice(RunwayCentrelinePointTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
