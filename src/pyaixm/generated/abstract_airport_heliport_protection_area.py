from dataclasses import dataclass

from pyaixm.generated.abstract_airport_heliport_protection_area_type import (
    AbstractAirportHeliportProtectionAreaType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class AbstractAirportHeliportProtectionArea(
    AbstractAirportHeliportProtectionAreaType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
