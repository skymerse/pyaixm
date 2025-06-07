from dataclasses import dataclass

from pyaixm.generated.air_traffic_control_service_type import (
    AirTrafficControlServiceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirTrafficControlService(AirTrafficControlServiceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
