from dataclasses import dataclass

from generated.altimeter_source_extension_type import (
    AltimeterSourceExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class AltimeterSourceExtension(AltimeterSourceExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
