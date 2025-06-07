from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.aerial_refuelling_time_slice import (
    AerialRefuellingTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AerialRefuellingTimeSlicePropertyType:
    aerial_refuelling_time_slice: Optional[AerialRefuellingTimeSlice] = field(
        default=None,
        metadata={
            "name": "AerialRefuellingTimeSlice",
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
