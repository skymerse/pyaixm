from dataclasses import dataclass

from pyaixm.generated.seaplane_ramp_site_extension_type import (
    SeaplaneRampSiteExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class SeaplaneRampSiteExtension(SeaplaneRampSiteExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
