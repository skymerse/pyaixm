from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_service_type import AbstractServiceType
from pyaixm.generated.search_rescue_service_time_slice_property_type import (
    SearchRescueServiceTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SearchRescueServiceType(AbstractServiceType):
    time_slice: Iterable[SearchRescueServiceTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
