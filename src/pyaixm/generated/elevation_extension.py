from dataclasses import dataclass

from pyaixm.generated.elevation_extension_type import ElevationExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class ElevationExtension(ElevationExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
