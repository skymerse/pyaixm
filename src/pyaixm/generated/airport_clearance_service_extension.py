from dataclasses import dataclass

from pyaixm.generated.airport_clearance_service_extension_type import (
    AirportClearanceServiceExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class AirportClearanceServiceExtension(AirportClearanceServiceExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
