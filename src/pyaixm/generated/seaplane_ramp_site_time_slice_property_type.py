from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.seaplane_ramp_site_time_slice import (
    SeaplaneRampSiteTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SeaplaneRampSiteTimeSlicePropertyType:
    seaplane_ramp_site_time_slice: Optional[SeaplaneRampSiteTimeSlice] = field(
        default=None,
        metadata={
            "name": "SeaplaneRampSiteTimeSlice",
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
