from dataclasses import dataclass

from generated.airport_heliport_availability_type import (
    AirportHeliportAvailabilityType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportHeliportAvailability(AirportHeliportAvailabilityType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
