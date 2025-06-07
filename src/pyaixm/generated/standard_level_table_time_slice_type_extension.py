from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.standard_level_table_extension import (
    StandardLevelTableExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandardLevelTableTimeSliceTypeExtension:
    class Meta:
        global_type = False

    standard_level_table_extension: Optional[StandardLevelTableExtension] = (
        field(
            default=None,
            metadata={
                "name": "StandardLevelTableExtension",
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
