from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_approach_leg_type import AbstractApproachLegType
from generated.arrival_feeder_leg_time_slice_property_type import (
    ArrivalFeederLegTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ArrivalFeederLegType(AbstractApproachLegType):
    time_slice: Iterable[ArrivalFeederLegTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
