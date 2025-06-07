from dataclasses import dataclass

from generated.touch_down_lift_off_safe_area_type import (
    TouchDownLiftOffSafeAreaType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TouchDownLiftOffSafeArea(TouchDownLiftOffSafeAreaType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
