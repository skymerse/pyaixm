from dataclasses import dataclass

from pyaixm.generated.floating_dock_site_type import FloatingDockSiteType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FloatingDockSite(FloatingDockSiteType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
