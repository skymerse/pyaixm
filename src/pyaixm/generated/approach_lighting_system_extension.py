from dataclasses import dataclass

from pyaixm.generated.approach_lighting_system_extension_type import (
    ApproachLightingSystemExtensionType,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class ApproachLightingSystemExtension(ApproachLightingSystemExtensionType):
    class Meta:
        namespace = "http://www.aixm.aero/schema/5.1/event"
