from dataclasses import dataclass

from pyaixm.generated.flight_restriction_level_type import (
    FlightRestrictionLevelType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1"


@dataclass
class FlightRestrictionLevel(FlightRestrictionLevelType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1"
