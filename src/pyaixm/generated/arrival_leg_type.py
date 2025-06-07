from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_segment_leg_type import AbstractSegmentLegType
from pyaixm.generated.arrival_leg_time_slice_property_type import (
    ArrivalLegTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ArrivalLegType(AbstractSegmentLegType):
    time_slice: Iterable[ArrivalLegTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
