from dataclasses import dataclass

from pyaixm.generated.airport_ground_service_extension_type import (
    AirportGroundServiceExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class AirportGroundServiceExtension(AirportGroundServiceExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
