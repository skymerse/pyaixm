from dataclasses import dataclass

from pyaixm.generated.airport_protection_area_marking_extension_type import (
    AirportProtectionAreaMarkingExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class AirportProtectionAreaMarkingExtension(
    AirportProtectionAreaMarkingExtensionType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
