from dataclasses import dataclass, field
from typing import Optional

from generated.geo_border_time_slice import GeoBorderTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GeoBorderTimeSlicePropertyType:
    geo_border_time_slice: Optional[GeoBorderTimeSlice] = field(
        default=None,
        metadata={
            "name": "GeoBorderTimeSlice",
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
