from dataclasses import dataclass

from generated.ground_traffic_control_service_extension_type import (
    GroundTrafficControlServiceExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class GroundTrafficControlServiceExtension(
    GroundTrafficControlServiceExtensionType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
