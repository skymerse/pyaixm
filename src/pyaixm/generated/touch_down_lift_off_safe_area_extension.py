from dataclasses import dataclass

from pyaixm.generated.touch_down_lift_off_safe_area_extension_type import (
    TouchDownLiftOffSafeAreaExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class TouchDownLiftOffSafeAreaExtension(TouchDownLiftOffSafeAreaExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
