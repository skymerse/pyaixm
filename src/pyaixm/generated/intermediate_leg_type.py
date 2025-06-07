from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_approach_leg_type import AbstractApproachLegType
from pyaixm.generated.intermediate_leg_time_slice_property_type import (
    IntermediateLegTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class IntermediateLegType(AbstractApproachLegType):
    time_slice: Iterable[IntermediateLegTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
