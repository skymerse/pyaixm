from dataclasses import dataclass, field
from typing import Optional

from generated.dmetime_slice import DmetimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DmetimeSlicePropertyType:
    class Meta:
        name = "DMETimeSlicePropertyType"

    dmetime_slice: Optional[DmetimeSlice] = field(
        default=None,
        metadata={
            "name": "DMETimeSlice",
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
