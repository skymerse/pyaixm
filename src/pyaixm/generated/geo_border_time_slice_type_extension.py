from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.geo_border_extension import GeoBorderExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GeoBorderTimeSliceTypeExtension:
    class Meta:
        global_type = False

    geo_border_extension: Optional[GeoBorderExtension] = field(
        default=None,
        metadata={
            "name": "GeoBorderExtension",
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
