from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.guidance_line_marking_extension import (
    GuidanceLineMarkingExtension,
)
from pyaixm.generated.marking_extension import MarkingExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GuidanceLineMarkingTimeSliceTypeExtension:
    class Meta:
        global_type = False

    guidance_line_marking_extension: Optional[GuidanceLineMarkingExtension] = (
        field(
            default=None,
            metadata={
                "name": "GuidanceLineMarkingExtension",
                "type": "Element",
                "namespace": "http://www.aixm.aero/schema/5.1/event",
            },
        )
    )
    marking_extension: Optional[MarkingExtension] = field(
        default=None,
        metadata={
            "name": "MarkingExtension",
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
