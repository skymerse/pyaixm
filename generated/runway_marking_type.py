from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_marking_type import AbstractMarkingType
from generated.runway_marking_time_slice_property_type import (
    RunwayMarkingTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayMarkingType(AbstractMarkingType):
    time_slice: Iterable[RunwayMarkingTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
