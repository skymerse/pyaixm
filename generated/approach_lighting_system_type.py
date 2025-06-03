from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_ground_light_system_type import (
    AbstractGroundLightSystemType,
)
from generated.approach_lighting_system_time_slice_property_type import (
    ApproachLightingSystemTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApproachLightingSystemType(AbstractGroundLightSystemType):
    time_slice: Iterable[ApproachLightingSystemTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
