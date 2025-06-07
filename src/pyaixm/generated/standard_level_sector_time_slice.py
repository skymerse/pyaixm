from dataclasses import dataclass

from pyaixm.generated.standard_level_sector_time_slice_type import (
    StandardLevelSectorTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardLevelSectorTimeSlice(StandardLevelSectorTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
