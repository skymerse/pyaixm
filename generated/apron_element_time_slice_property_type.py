from dataclasses import dataclass, field
from typing import Optional

from generated.apron_element_time_slice import ApronElementTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ApronElementTimeSlicePropertyType:
    apron_element_time_slice: Optional[ApronElementTimeSlice] = field(
        default=None,
        metadata={
            "name": "ApronElementTimeSlice",
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
