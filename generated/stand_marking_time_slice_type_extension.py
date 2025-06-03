from dataclasses import dataclass, field
from typing import Optional

from generated.marking_extension import MarkingExtension
from generated.stand_marking_extension import StandMarkingExtension

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class StandMarkingTimeSliceTypeExtension:
    class Meta:
        global_type = False

    stand_marking_extension: Optional[StandMarkingExtension] = field(
        default=None,
        metadata={
            "name": "StandMarkingExtension",
            "type": "Element",
            "namespace": "http://www.aixm.aero/schema/5.1/event",
        },
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
