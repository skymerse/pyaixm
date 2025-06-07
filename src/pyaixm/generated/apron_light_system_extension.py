from dataclasses import dataclass

from generated.apron_light_system_extension_type import (
    ApronLightSystemExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class ApronLightSystemExtension(ApronLightSystemExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
