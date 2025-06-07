from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.deicing_area_marking_extension import (
    DeicingAreaMarkingExtension,
)
from pyaixm.generated.marking_extension import MarkingExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class DeicingAreaMarkingTimeSliceTypeExtension:
    class Meta:
        global_type = False

    deicing_area_marking_extension: Optional[DeicingAreaMarkingExtension] = (
        field(
            default=None,
            metadata={
                "name": "DeicingAreaMarkingExtension",
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
