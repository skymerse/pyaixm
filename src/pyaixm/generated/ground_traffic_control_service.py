from dataclasses import dataclass

from pyaixm.generated.ground_traffic_control_service_type import (
    GroundTrafficControlServiceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class GroundTrafficControlService(GroundTrafficControlServiceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
