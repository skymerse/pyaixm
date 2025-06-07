from dataclasses import dataclass

from pyaixm.generated.floating_dock_site_extension_type import (
    FloatingDockSiteExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class FloatingDockSiteExtension(FloatingDockSiteExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
