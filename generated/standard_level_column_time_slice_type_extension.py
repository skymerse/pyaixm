from dataclasses import dataclass, field
from typing import Optional

from generated.standard_level_column_extension import (
    StandardLevelColumnExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardLevelColumnTimeSliceTypeExtension:
    class Meta:
        global_type = False

    standard_level_column_extension: Optional[StandardLevelColumnExtension] = (
        field(
            default=None,
            metadata={
                "name": "StandardLevelColumnExtension",
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
