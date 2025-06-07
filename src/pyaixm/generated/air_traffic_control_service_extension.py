from dataclasses import dataclass

from pyaixm.generated.air_traffic_control_service_extension_type import (
    AirTrafficControlServiceExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class AirTrafficControlServiceExtension(AirTrafficControlServiceExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
