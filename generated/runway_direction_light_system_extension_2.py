from dataclasses import dataclass

from generated.runway_direction_light_system_extension_type_2 import (
    RunwayDirectionLightSystemExtensionType2,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class RunwayDirectionLightSystemExtension2(
    RunwayDirectionLightSystemExtensionType2
):
    class Meta:
        name = "RunwayDirectionLightSystemExtension"
        namespace = "urn:us.gov.dot.faa.aim.fns"
