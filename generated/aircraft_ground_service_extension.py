from dataclasses import dataclass

from generated.aircraft_ground_service_extension_type import (
    AircraftGroundServiceExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class AircraftGroundServiceExtension(AircraftGroundServiceExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
