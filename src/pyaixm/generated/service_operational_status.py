from dataclasses import dataclass

from pyaixm.generated.service_operational_status_type import (
    ServiceOperationalStatusType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class ServiceOperationalStatus(ServiceOperationalStatusType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
