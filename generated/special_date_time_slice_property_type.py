from dataclasses import dataclass, field
from typing import Optional

from generated.special_date_time_slice import SpecialDateTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SpecialDateTimeSlicePropertyType:
    special_date_time_slice: Optional[SpecialDateTimeSlice] = field(
        default=None,
        metadata={
            "name": "SpecialDateTimeSlice",
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
