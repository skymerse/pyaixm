from dataclasses import dataclass

from pyaixm.generated.airport_heliport_collocation_extension_type import (
    AirportHeliportCollocationExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class AirportHeliportCollocationExtension(
    AirportHeliportCollocationExtensionType
):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
