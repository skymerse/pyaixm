from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.standard_level_sector_time_slice import (
    StandardLevelSectorTimeSlice,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardLevelSectorTimeSlicePropertyType:
    standard_level_sector_time_slice: Optional[
        StandardLevelSectorTimeSlice
    ] = field(
        default=None,
        metadata={
            "name": "StandardLevelSectorTimeSlice",
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
