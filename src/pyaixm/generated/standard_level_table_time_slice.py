from dataclasses import dataclass

from pyaixm.generated.standard_level_table_time_slice_type import (
    StandardLevelTableTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardLevelTableTimeSlice(StandardLevelTableTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
