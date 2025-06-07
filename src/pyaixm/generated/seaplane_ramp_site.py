from dataclasses import dataclass

from pyaixm.generated.seaplane_ramp_site_type import SeaplaneRampSiteType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SeaplaneRampSite(SeaplaneRampSiteType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
