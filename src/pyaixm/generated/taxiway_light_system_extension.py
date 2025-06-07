from dataclasses import dataclass

from generated.taxiway_light_system_extension_type import (
    TaxiwayLightSystemExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class TaxiwayLightSystemExtension(TaxiwayLightSystemExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
