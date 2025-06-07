from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_marking_type import AbstractMarkingType
from pyaixm.generated.guidance_line_marking_time_slice_property_type import (
    GuidanceLineMarkingTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GuidanceLineMarkingType(AbstractMarkingType):
    time_slice: Iterable[GuidanceLineMarkingTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
