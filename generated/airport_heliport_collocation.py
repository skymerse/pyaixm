from dataclasses import dataclass

from generated.airport_heliport_collocation_type import (
    AirportHeliportCollocationType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportHeliportCollocation(AirportHeliportCollocationType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
