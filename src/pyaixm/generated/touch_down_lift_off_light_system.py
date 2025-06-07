from dataclasses import dataclass

from pyaixm.generated.touch_down_lift_off_light_system_type import (
    TouchDownLiftOffLightSystemType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class TouchDownLiftOffLightSystem(TouchDownLiftOffLightSystemType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
