from dataclasses import dataclass

from generated.airport_heliport_protection_area_extension_type import (
    AirportHeliportProtectionAreaExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class AirportHeliportProtectionAreaExtension(
    AirportHeliportProtectionAreaExtensionType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
