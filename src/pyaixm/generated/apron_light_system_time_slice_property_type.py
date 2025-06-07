from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.apron_light_system_time_slice import (
    ApronLightSystemTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApronLightSystemTimeSlicePropertyType:
    apron_light_system_time_slice: Optional[ApronLightSystemTimeSlice] = field(
        default=None,
        metadata={
            "name": "ApronLightSystemTimeSlice",
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
