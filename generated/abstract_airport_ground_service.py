from dataclasses import dataclass

from generated.abstract_airport_ground_service_type import (
    AbstractAirportGroundServiceType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractAirportGroundService(AbstractAirportGroundServiceType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
