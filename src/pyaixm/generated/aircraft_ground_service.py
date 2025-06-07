from dataclasses import dataclass

from generated.aircraft_ground_service_type import AircraftGroundServiceType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AircraftGroundService(AircraftGroundServiceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
