from dataclasses import dataclass

from pyaixm.generated.arresting_gear_time_slice_type import (
    ArrestingGearTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ArrestingGearTimeSlice(ArrestingGearTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
