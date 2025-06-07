from dataclasses import dataclass

from pyaixm.generated.azimuth_extension_type import AzimuthExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class AzimuthExtension(AzimuthExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
