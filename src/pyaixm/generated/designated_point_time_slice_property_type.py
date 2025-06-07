from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.designated_point_time_slice import (
    DesignatedPointTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DesignatedPointTimeSlicePropertyType:
    designated_point_time_slice: Optional[DesignatedPointTimeSlice] = field(
        default=None,
        metadata={
            "name": "DesignatedPointTimeSlice",
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
