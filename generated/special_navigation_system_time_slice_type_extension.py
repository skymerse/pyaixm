from dataclasses import dataclass, field
from typing import Optional

from generated.special_navigation_system_extension import (
    SpecialNavigationSystemExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SpecialNavigationSystemTimeSliceTypeExtension:
    class Meta:
        global_type = False

    special_navigation_system_extension: Optional[
        SpecialNavigationSystemExtension
    ] = field(
        default=None,
        metadata={
            "name": "SpecialNavigationSystemExtension",
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
