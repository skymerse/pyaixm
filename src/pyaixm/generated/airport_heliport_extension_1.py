from dataclasses import dataclass

from pyaixm.generated.airport_heliport_extension_type_1 import (
    AirportHeliportExtensionType1,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class AirportHeliportExtension1(AirportHeliportExtensionType1):
    class Meta:
        name = "AirportHeliportExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
