from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_marking_type import AbstractMarkingType
from generated.deicing_area_marking_time_slice_property_type import (
    DeicingAreaMarkingTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DeicingAreaMarkingType(AbstractMarkingType):
    time_slice: Iterable[DeicingAreaMarkingTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
