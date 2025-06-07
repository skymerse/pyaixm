from dataclasses import dataclass, field
from typing import Optional

from generated.guidance_line_extension import GuidanceLineExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GuidanceLineTimeSliceTypeExtension:
    class Meta:
        global_type = False

    guidance_line_extension: Optional[GuidanceLineExtension] = field(
        default=None,
        metadata={
            "name": "GuidanceLineExtension",
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
