from dataclasses import dataclass

from generated.touch_down_lift_off_marking_extension_type import (
    TouchDownLiftOffMarkingExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class TouchDownLiftOffMarkingExtension(TouchDownLiftOffMarkingExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
