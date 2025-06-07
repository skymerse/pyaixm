from dataclasses import dataclass

from pyaixm.generated.airport_hot_spot_extension_type import (
    AirportHotSpotExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class AirportHotSpotExtension(AirportHotSpotExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
