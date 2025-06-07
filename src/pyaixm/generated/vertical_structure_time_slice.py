from dataclasses import dataclass

from generated.vertical_structure_time_slice_type import (
    VerticalStructureTimeSliceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class VerticalStructureTimeSlice(VerticalStructureTimeSliceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
