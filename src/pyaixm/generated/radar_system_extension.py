from dataclasses import dataclass

from pyaixm.generated.radar_system_extension_type import (
    RadarSystemExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class RadarSystemExtension(RadarSystemExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
