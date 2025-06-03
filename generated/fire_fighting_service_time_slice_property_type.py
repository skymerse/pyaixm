from dataclasses import dataclass, field
from typing import Optional

from generated.fire_fighting_service_time_slice import (
    FireFightingServiceTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FireFightingServiceTimeSlicePropertyType:
    fire_fighting_service_time_slice: Optional[
        FireFightingServiceTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "FireFightingServiceTimeSlice",
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
