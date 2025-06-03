from dataclasses import dataclass, field
from typing import Optional

from generated.circling_area_extension import CirclingAreaExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class CirclingAreaTimeSliceTypeExtension:
    class Meta:
        global_type = False

    circling_area_extension: Optional[CirclingAreaExtension] = field(
        default=None,
        metadata={
            "name": "CirclingAreaExtension",
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
