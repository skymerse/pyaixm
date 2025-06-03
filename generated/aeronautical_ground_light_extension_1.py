from dataclasses import dataclass

from generated.aeronautical_ground_light_extension_type_1 import (
    AeronauticalGroundLightExtensionType1,
)

__NAMESPACE__ = "http://www.aixm.aero/schema/5.1/event"


@dataclass
class AeronauticalGroundLightExtension1(AeronauticalGroundLightExtensionType1):
    class Meta:
        name = "AeronauticalGroundLightExtension"
        namespace = "http://www.aixm.aero/schema/5.1/event"
