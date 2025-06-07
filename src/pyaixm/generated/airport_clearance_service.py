from dataclasses import dataclass

from pyaixm.generated.airport_clearance_service_type import (
    AirportClearanceServiceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportClearanceService(AirportClearanceServiceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
