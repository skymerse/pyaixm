from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_approach_leg_type import AbstractApproachLegType
from generated.initial_leg_time_slice_property_type import (
    InitialLegTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class InitialLegType(AbstractApproachLegType):
    time_slice: Iterable[InitialLegTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
