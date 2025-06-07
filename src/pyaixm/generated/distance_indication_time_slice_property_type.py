from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.distance_indication_time_slice import (
    DistanceIndicationTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DistanceIndicationTimeSlicePropertyType:
    distance_indication_time_slice: Optional[DistanceIndicationTimeSlice] = (
        field(
            default=None,
            metadata={
                "name": "DistanceIndicationTimeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "required": True,
            },
        )
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
