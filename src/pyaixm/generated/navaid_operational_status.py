from dataclasses import dataclass

from generated.navaid_operational_status_type import (
    NavaidOperationalStatusType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class NavaidOperationalStatus(NavaidOperationalStatusType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
