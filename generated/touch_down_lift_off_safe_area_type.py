from collections.abc import Iterable
from dataclasses import dataclass, field

from generated.abstract_airport_heliport_protection_area_type import (
    AbstractAirportHeliportProtectionAreaType,
)
from generated.touch_down_lift_off_safe_area_time_slice_property_type import (
    TouchDownLiftOffSafeAreaTimeSlicePropertyType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TouchDownLiftOffSafeAreaType(AbstractAirportHeliportProtectionAreaType):
    time_slice: Iterable[TouchDownLiftOffSafeAreaTimeSlicePropertyType] = (
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
