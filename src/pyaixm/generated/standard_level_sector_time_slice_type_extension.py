from dataclasses import dataclass, field
from typing import Optional

from generated.standard_level_sector_extension import (
    StandardLevelSectorExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardLevelSectorTimeSliceTypeExtension:
    class Meta:
        global_type = False

    standard_level_sector_extension: Optional[StandardLevelSectorExtension] = (
        field(
            default=None,
            metadata={
                "name": "StandardLevelSectorExtension",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1/event",
            },
        )
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
