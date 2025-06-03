from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_aixmfeature_type import AbstractAixmfeatureType
from generated.circling_area_time_slice_property_type import (
    CirclingAreaTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CirclingAreaType(AbstractAixmfeatureType):
    time_slice: Iterable[CirclingAreaTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
