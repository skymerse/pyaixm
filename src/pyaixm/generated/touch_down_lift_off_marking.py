from dataclasses import dataclass

from generated.touch_down_lift_off_marking_type import (
    TouchDownLiftOffMarkingType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TouchDownLiftOffMarking(TouchDownLiftOffMarkingType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
