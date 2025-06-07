from dataclasses import dataclass

from pyaixm.generated.touch_down_lift_off_type import TouchDownLiftOffType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TouchDownLiftOff(TouchDownLiftOffType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
