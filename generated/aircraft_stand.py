from dataclasses import dataclass

from generated.aircraft_stand_type import AircraftStandType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AircraftStand(AircraftStandType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
