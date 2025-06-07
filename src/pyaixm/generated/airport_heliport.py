from dataclasses import dataclass

from generated.airport_heliport_type import AirportHeliportType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AirportHeliport(AirportHeliportType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
