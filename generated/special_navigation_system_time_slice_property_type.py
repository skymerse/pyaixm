from dataclasses import dataclass, field
from typing import Optional

from generated.special_navigation_system_time_slice import (
    SpecialNavigationSystemTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SpecialNavigationSystemTimeSlicePropertyType:
    special_navigation_system_time_slice: Optional[
        SpecialNavigationSystemTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "SpecialNavigationSystemTimeSlice",
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
