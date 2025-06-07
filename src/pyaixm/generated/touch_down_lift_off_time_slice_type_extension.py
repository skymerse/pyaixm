from dataclasses import dataclass, field
from typing import Optional

from pyaixm.generated.touch_down_lift_off_extension import (
    TouchDownLiftOffExtension,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TouchDownLiftOffTimeSliceTypeExtension:
    class Meta:
        global_type = False

    touch_down_lift_off_extension: Optional[TouchDownLiftOffExtension] = field(
        default=None,
        metadata={
            "name": "TouchDownLiftOffExtension",
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
