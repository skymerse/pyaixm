from dataclasses import dataclass

from pyaixm.generated.touch_down_lift_off_extension_type import (
    TouchDownLiftOffExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class TouchDownLiftOffExtension(TouchDownLiftOffExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
