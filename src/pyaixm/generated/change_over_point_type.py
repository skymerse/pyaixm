from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_aixmfeature_type import AbstractAixmfeatureType
from pyaixm.generated.change_over_point_time_slice_property_type import (
    ChangeOverPointTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ChangeOverPointType(AbstractAixmfeatureType):
    time_slice: Iterable[ChangeOverPointTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
