from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.floating_dock_site_time_slice import (
    FloatingDockSiteTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FloatingDockSiteTimeSlicePropertyType:
    floating_dock_site_time_slice: Optional[FloatingDockSiteTimeSlice] = field(
        default=None,
        metadata={
            "name": "FloatingDockSiteTimeSlice",
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
