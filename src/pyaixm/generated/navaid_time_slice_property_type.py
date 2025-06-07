from dataclasses import dataclass, field
from typing import Optional

from generated.navaid_time_slice import NavaidTimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavaidTimeSlicePropertyType:
    navaid_time_slice: Optional[NavaidTimeSlice] = field(
        default=None,
        metadata={
            "name": "NavaidTimeSlice",
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
