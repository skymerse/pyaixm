from dataclasses import dataclass, field
from typing import Optional

from generated.sdftime_slice import SdftimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class SdftimeSlicePropertyType:
    class Meta:
        name = "SDFTimeSlicePropertyType"

    sdftime_slice: Optional[SdftimeSlice] = field(
        default=None,
        metadata={
            "name": "SDFTimeSlice",
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
