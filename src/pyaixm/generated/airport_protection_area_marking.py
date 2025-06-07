from dataclasses import dataclass

from generated.airport_protection_area_marking_type import (
    AirportProtectionAreaMarkingType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportProtectionAreaMarking(AirportProtectionAreaMarkingType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
