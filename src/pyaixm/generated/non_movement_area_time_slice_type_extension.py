from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.non_movement_area_extension import (
    NonMovementAreaExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NonMovementAreaTimeSliceTypeExtension:
    class Meta:
        global_type = False

    non_movement_area_extension: Optional[NonMovementAreaExtension] = field(
        default=None,
        metadata={
            "name": "NonMovementAreaExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
