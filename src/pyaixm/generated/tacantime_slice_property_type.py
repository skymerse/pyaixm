from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.tacantime_slice import TacantimeSlice

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TacantimeSlicePropertyType:
    class Meta:
        name = "TACANTimeSlicePropertyType"

    tacantime_slice: Optional[TacantimeSlice] = field(
        default=None,
        metadata={
            "name": "TACANTimeSlice",
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
