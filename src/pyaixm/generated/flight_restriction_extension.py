from dataclasses import dataclass

from pyaixm.generated.flight_restriction_extension_type import (
    FlightRestrictionExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class FlightRestrictionExtension(FlightRestrictionExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
