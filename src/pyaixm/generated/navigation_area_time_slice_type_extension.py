from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.navigation_area_extension import NavigationAreaExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavigationAreaTimeSliceTypeExtension:
    class Meta:
        global_type = False

    navigation_area_extension: Optional[NavigationAreaExtension] = field(
        default=None,
        metadata={
            "name": "NavigationAreaExtension",
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
