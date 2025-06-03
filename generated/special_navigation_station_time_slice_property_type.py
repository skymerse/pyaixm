from dataclasses import dataclass, field
from typing import Optional

from generated.special_navigation_station_time_slice import (
    SpecialNavigationStationTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SpecialNavigationStationTimeSlicePropertyType:
    special_navigation_station_time_slice: Optional[
        SpecialNavigationStationTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "SpecialNavigationStationTimeSlice",
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
