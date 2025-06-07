from dataclasses import dataclass

from pyaixm.generated.safe_altitude_area_extension_type import (
    SafeAltitudeAreaExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class SafeAltitudeAreaExtension(SafeAltitudeAreaExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
