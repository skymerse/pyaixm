from dataclasses import dataclass, field
from typing import Optional

from generated.standard_level_column_time_slice import (
    StandardLevelColumnTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardLevelColumnTimeSlicePropertyType:
    standard_level_column_time_slice: Optional[
        StandardLevelColumnTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "StandardLevelColumnTimeSlice",
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
