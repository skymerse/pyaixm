from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_marking_type import AbstractMarkingType
from pyaixm.generated.apron_marking_time_slice_property_type import (
    ApronMarkingTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApronMarkingType(AbstractMarkingType):
    time_slice: Iterable[ApronMarkingTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
