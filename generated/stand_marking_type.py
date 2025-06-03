from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_marking_type import AbstractMarkingType
from generated.stand_marking_time_slice_property_type import (
    StandMarkingTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandMarkingType(AbstractMarkingType):
    time_slice: Iterable[StandMarkingTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
