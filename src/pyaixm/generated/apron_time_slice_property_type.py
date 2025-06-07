from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.apron_time_slice import ApronTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApronTimeSlicePropertyType:
    apron_time_slice: Optional[ApronTimeSlice] = field(
        default=None,
        metadata={
            "name": "ApronTimeSlice",
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
