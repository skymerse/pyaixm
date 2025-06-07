from dataclasses import dataclass

from pyaixm.generated.airspace_border_crossing_extension_type import (
    AirspaceBorderCrossingExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class AirspaceBorderCrossingExtension(AirspaceBorderCrossingExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
