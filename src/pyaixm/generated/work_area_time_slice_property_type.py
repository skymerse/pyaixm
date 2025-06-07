from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.work_area_time_slice import WorkAreaTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class WorkAreaTimeSlicePropertyType:
    work_area_time_slice: Optional[WorkAreaTimeSlice] = field(
        default=None,
        metadata={
            "name": "WorkAreaTimeSlice",
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
