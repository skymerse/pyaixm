from dataclasses import dataclass

from pyaixm.generated.abstract_direct_flight_type import (
    AbstractDirectFlightType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractDirectFlight(AbstractDirectFlightType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
