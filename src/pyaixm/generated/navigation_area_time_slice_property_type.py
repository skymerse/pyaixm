from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.navigation_area_time_slice import NavigationAreaTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavigationAreaTimeSlicePropertyType:
    navigation_area_time_slice: Optional[NavigationAreaTimeSlice] = field(
        default=None,
        metadata={
            "name": "NavigationAreaTimeSlice",
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
