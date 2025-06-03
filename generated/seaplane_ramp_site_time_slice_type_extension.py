from dataclasses import dataclass, field
from typing import Optional

from generated.seaplane_ramp_site_extension import SeaplaneRampSiteExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SeaplaneRampSiteTimeSliceTypeExtension:
    class Meta:
        global_type = False

    seaplane_ramp_site_extension: Optional[SeaplaneRampSiteExtension] = field(
        default=None,
        metadata={
            "name": "SeaplaneRampSiteExtension",
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
