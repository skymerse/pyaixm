from dataclasses import dataclass

from pyaixm.generated.airspace_extension_type import AirspaceExtensionType

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class AirspaceExtension(AirspaceExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
