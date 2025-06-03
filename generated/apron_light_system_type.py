from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_ground_light_system_type import (
    AbstractGroundLightSystemType,
)
from generated.apron_light_system_time_slice_property_type import (
    ApronLightSystemTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApronLightSystemType(AbstractGroundLightSystemType):
    time_slice: Iterable[ApronLightSystemTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
