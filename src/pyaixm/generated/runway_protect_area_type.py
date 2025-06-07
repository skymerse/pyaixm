from collections.abc import Iterable
from dataclasses import dataclass, field

from pyaixm.generated.abstract_airport_heliport_protection_area_type import (
    AbstractAirportHeliportProtectionAreaType,
)
from pyaixm.generated.runway_protect_area_time_slice_property_type import (
    RunwayProtectAreaTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class RunwayProtectAreaType(AbstractAirportHeliportProtectionAreaType):
    time_slice: Iterable[RunwayProtectAreaTimeSlicePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "timeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "min_occurs": 1,
        },
    )
