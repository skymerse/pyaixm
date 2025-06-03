from dataclasses import dataclass, field
from typing import Optional

from generated.floating_dock_site_extension import FloatingDockSiteExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FloatingDockSiteTimeSliceTypeExtension:
    class Meta:
        global_type = False

    floating_dock_site_extension: Optional[FloatingDockSiteExtension] = field(
        default=None,
        metadata={
            "name": "FloatingDockSiteExtension",
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
