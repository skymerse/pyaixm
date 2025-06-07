from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.standard_level_table_time_slice import (
    StandardLevelTableTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardLevelTableTimeSlicePropertyType:
    standard_level_table_time_slice: Optional[StandardLevelTableTimeSlice] = (
        field(
            default=None,
            metadata={
                "name": "StandardLevelTableTimeSlice",
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
