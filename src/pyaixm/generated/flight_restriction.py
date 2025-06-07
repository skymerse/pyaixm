from dataclasses import dataclass

from generated.flight_restriction_type import FlightRestrictionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FlightRestriction(FlightRestrictionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
