from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_segment_leg_type import AbstractSegmentLegType
from generated.departure_leg_time_slice_property_type import (
    DepartureLegTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DepartureLegType(AbstractSegmentLegType):
    time_slice: Iterable[DepartureLegTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
