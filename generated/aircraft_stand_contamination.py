from dataclasses import dataclass

from generated.aircraft_stand_contamination_type import (
    AircraftStandContaminationType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AircraftStandContamination(AircraftStandContaminationType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
