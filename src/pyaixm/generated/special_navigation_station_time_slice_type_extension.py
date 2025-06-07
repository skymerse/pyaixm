from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.special_navigation_station_extension import (
    SpecialNavigationStationExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SpecialNavigationStationTimeSliceTypeExtension:
    class Meta:
        global_type = False

    special_navigation_station_extension: Optional[
        SpecialNavigationStationExtension
    ] = field(
        default=None,
        metadata={
            "name": "SpecialNavigationStationExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
