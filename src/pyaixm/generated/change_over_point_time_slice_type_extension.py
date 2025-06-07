from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.change_over_point_extension import (
    ChangeOverPointExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ChangeOverPointTimeSliceTypeExtension:
    class Meta:
        global_type = False

    change_over_point_extension: Optional[ChangeOverPointExtension] = field(
        default=None,
        metadata={
            "name": "ChangeOverPointExtension",
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
