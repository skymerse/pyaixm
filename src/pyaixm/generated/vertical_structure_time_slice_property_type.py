from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.vertical_structure_time_slice import (
    VerticalStructureTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class VerticalStructureTimeSlicePropertyType:
    vertical_structure_time_slice: Optional[VerticalStructureTimeSlice] = (
        field(
            default=None,
            metadata={
                "name": "VerticalStructureTimeSlice",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1",
                "required": True,
            },
        )
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
