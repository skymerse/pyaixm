from dataclasses import dataclass

from generated.standard_level_column_time_slice_type import (
    StandardLevelColumnTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardLevelColumnTimeSlice(StandardLevelColumnTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
