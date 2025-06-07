from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.marking_extension import MarkingExtension
from pyaixm.generated.touch_down_lift_off_marking_extension import (
    TouchDownLiftOffMarkingExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TouchDownLiftOffMarkingTimeSliceTypeExtension:
    class Meta:
        global_type = False

    touch_down_lift_off_marking_extension: Optional[
        TouchDownLiftOffMarkingExtension
    ] = field(
        default=None,
        metadata={
            "name": "TouchDownLiftOffMarkingExtension",
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
