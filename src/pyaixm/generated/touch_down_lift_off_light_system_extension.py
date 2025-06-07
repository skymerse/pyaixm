from dataclasses import dataclass

from pyaixm.generated.touch_down_lift_off_light_system_extension_type import (
    TouchDownLiftOffLightSystemExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class TouchDownLiftOffLightSystemExtension(
    TouchDownLiftOffLightSystemExtensionType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
