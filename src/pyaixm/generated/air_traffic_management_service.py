from dataclasses import dataclass

from pyaixm.generated.air_traffic_management_service_type import (
    AirTrafficManagementServiceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirTrafficManagementService(AirTrafficManagementServiceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
