from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_aixmfeature_type import AbstractAixmfeatureType
from generated.runway_direction_time_slice_property_type import (
    RunwayDirectionTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayDirectionType(AbstractAixmfeatureType):
    time_slice: Iterable[RunwayDirectionTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
