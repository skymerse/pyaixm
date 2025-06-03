from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_aixmfeature_type import AbstractAixmfeatureType
from generated.pilot_controlled_lighting_time_slice_property_type import (
    PilotControlledLightingTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class PilotControlledLightingType(AbstractAixmfeatureType):
    time_slice: Iterable[PilotControlledLightingTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
