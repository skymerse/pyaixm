from dataclasses import dataclass

from generated.aeronautical_ground_light_extension_type_2 import (
    AeronauticalGroundLightExtensionType2,
)

__NAMESPACE__ = "urn:us.gov.dot.faa.aim.fns"


@dataclass
class AeronauticalGroundLightExtension2(AeronauticalGroundLightExtensionType2):
    class Meta:
        name = "AeronauticalGroundLightExtension"
        namespace = "urn:us.gov.dot.faa.aim.fns"
