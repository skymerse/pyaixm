from dataclasses import dataclass, field
from typing import Optional

from generated.unit_time_slice import UnitTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class UnitTimeSlicePropertyType:
    unit_time_slice: Optional[UnitTimeSlice] = field(
        default=None,
        metadata={
            "name": "UnitTimeSlice",
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
