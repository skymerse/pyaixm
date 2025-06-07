from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_marking_type import AbstractMarkingType
from pyaixm.generated.touch_down_lift_off_marking_time_slice_property_type import (
    TouchDownLiftOffMarkingTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TouchDownLiftOffMarkingType(AbstractMarkingType):
    time_slice: Iterable[TouchDownLiftOffMarkingTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
