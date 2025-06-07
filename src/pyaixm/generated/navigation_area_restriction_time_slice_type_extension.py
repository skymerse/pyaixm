from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.navigation_area_restriction_extension import (
    NavigationAreaRestrictionExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavigationAreaRestrictionTimeSliceTypeExtension:
    class Meta:
        global_type = False

    navigation_area_restriction_extension: Optional[
        NavigationAreaRestrictionExtension
    ] = field(
        default=None,
        metadata={
            "name": "NavigationAreaRestrictionExtension",
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
