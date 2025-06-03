from dataclasses import dataclass

from generated.touch_down_lift_off_contamination_type import (
    TouchDownLiftOffContaminationType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TouchDownLiftOffContamination(TouchDownLiftOffContaminationType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
