from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_approach_leg_type import AbstractApproachLegType
from pyaixm.generated.missed_approach_leg_time_slice_property_type import (
    MissedApproachLegTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class MissedApproachLegType(AbstractApproachLegType):
    time_slice: Iterable[MissedApproachLegTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
