from dataclasses import dataclass

from pyaixm.generated.air_traffic_management_service_extension_type import (
    AirTrafficManagementServiceExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class AirTrafficManagementServiceExtension(
    AirTrafficManagementServiceExtensionType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
