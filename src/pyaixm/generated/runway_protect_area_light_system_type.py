from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_ground_light_system_type import (
    AbstractGroundLightSystemType,
)
from pyaixm.generated.runway_protect_area_light_system_time_slice_property_type import (
    RunwayProtectAreaLightSystemTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayProtectAreaLightSystemType(AbstractGroundLightSystemType):
    time_slice: Iterable[RunwayProtectAreaLightSystemTimeSlicePropertyType] = (
        field(
            default_factory=list,
            metadata={
                "name": "timeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "min_occurs": 1,
            },
        )
    )
