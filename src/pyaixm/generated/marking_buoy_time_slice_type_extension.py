from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.marking_buoy_extension import MarkingBuoyExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class MarkingBuoyTimeSliceTypeExtension:
    class Meta:
        global_type = False

    marking_buoy_extension: Optional[MarkingBuoyExtension] = field(
        default=None,
        metadata={
            "name": "MarkingBuoyExtension",
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
