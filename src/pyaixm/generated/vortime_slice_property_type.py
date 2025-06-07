from dataclasses import dataclass, field
from typing import Optional

from generated.vortime_slice import VortimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class VortimeSlicePropertyType:
    class Meta:
        name = "VORTimeSlicePropertyType"

    vortime_slice: Optional[VortimeSlice] = field(
        default=None,
        metadata={
            "name": "VORTimeSlice",
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
