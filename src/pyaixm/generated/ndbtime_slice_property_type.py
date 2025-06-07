from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.ndbtime_slice import NdbtimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NdbtimeSlicePropertyType:
    class Meta:
        name = "NDBTimeSlicePropertyType"

    ndbtime_slice: Optional[NdbtimeSlice] = field(
        default=None,
        metadata={
            "name": "NDBTimeSlice",
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
