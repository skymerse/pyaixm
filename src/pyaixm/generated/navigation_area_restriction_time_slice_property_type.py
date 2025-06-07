from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.navigation_area_restriction_time_slice import (
    NavigationAreaRestrictionTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavigationAreaRestrictionTimeSlicePropertyType:
    navigation_area_restriction_time_slice: Optional[
        NavigationAreaRestrictionTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "NavigationAreaRestrictionTimeSlice",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1",
            "required": True,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
